#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
main.py - application entry point.

Per the "modularize your massive file" advice: this file now contains
ONLY startup/orchestration. All the actual logic lives in the numbered
files in this same folder (01_config_and_db.py ... 44_response_bank_
topic_aliases.py) - including the response-bank data files, which used
to live in their own response_banks/ subfolder and have since been
flattened back into this same folder as plain numbered files (33-44),
same as everything else, so there's only ever ONE folder to keep
together - no subfolders to worry about losing track of.

WHY A LOADER INSTEAD OF PLAIN IMPORTS:
The original file was one shared global namespace end-to-end - classes
in Section 9 reference classes from Section 6G, response handlers
reference response-bank dicts from Section 8, etc., with no imports
because they never needed any. Splitting that into fully independent
modules would require hand-tracing every one of those cross-references
across 60k+ lines, which is exactly the kind of change likely to
silently break something. So instead, this loader execs every file, in
the SAME order the original monolith defined things in, into one shared
namespace - every existing cross-reference keeps working unmodified,
while each file on disk is now small enough to open, scroll, and edit
in Pydroid 3 without lag. Run with `python main.py` for the plain-text
chat, or `python main.py --test` for the self-test.
"""
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))

_MODULE_FILES = [
    "00_endpoints.py",
    "01_config_and_db.py",
    "02_memory_and_logging.py",
    "03_datetime_engine.py",
    "04_creative_writing.py",
    "05_fun_extras.py",
    "06_text_number_tools.py",
    "07_continuity_and_tone.py",
    "08_hangman.py",
    "09_sklearn_tools.py",
    "10_neural_networks.py",
    "32_deep_networks.py",
    "11_llm_hybrid.py",
    "12_intent_engine.py",
    # New feature modules - must load before 14_chatbot_core.py, which
    # instantiates them in ChatBot.__init__.
    "22_games_rps.py",
    "23_games_tictactoe.py",
    "24_dice_and_coin.py",
    "25_cipher_tools.py",
    "26_billsplit_tip.py",
    "27_name_generator.py",
    "28_ascii_art.py",
    "29_markdown_table.py",
    "30_countdown_dashboard.py",
    "31_word_games.py",
    # Response-bank data (formerly response_banks/*.py in their own
    # subfolder) - loads right after the intent engine and before the
    # main ChatBot class, matching the original Section 7C -> Section
    # 8 -> Section 9 order. Just plain files now, no special-case
    # subfolder loader needed.
    "33_response_bank_core.py",
    "34_response_bank_ext1.py",
    "35_response_bank_ext2.py",
    "36_response_bank_ext3_casual.py",
    "37_response_bank_ext4_sheng.py",
    "38_response_bank_ext5.py",
    "39_response_bank_ext6.py",
    "40_response_bank_ext7.py",
    "41_response_bank_ext8.py",
    "42_response_bank_ext9.py",
    "43_response_bank_ext10.py",
    "44_response_bank_topic_aliases.py",
    # Auto-templated 5x volume multiplier (Section 8-EXT11 through
    # EXT18) - generated content, disclosed as such in each file's own
    # docstring; see there for the method. Must load AFTER the banks
    # above, since each of these just extends the dicts those files
    # already defined.
    "45_response_bank_ext_generated.py",
    "14_chatbot_core.py",
    "53_speech_recognition.py",
    
    "16_vision.py",
    "17_api_connectors.py",
    "18_qr_code.py",
    "19_tool_calling.py",
    "20_language_models.py",
    "21_main_and_tests.py",
]


def _load_all(run_name="__main__"):
    """Execs every module file, in original order, into one shared
    namespace (this dict), then returns it. This dict ends up holding
    every class/function/constant the original single file defined."""
    shared_globals = {"__name__": run_name, "__file__": __file__}

    for fname in _MODULE_FILES:
        path = os.path.join(_HERE, fname)
        with open(path, "r", encoding="utf-8") as f:
            code = compile(f.read(), path, "exec")
        exec(code, shared_globals)

    return shared_globals


if __name__ == "__main__":
    # 21_main_and_tests.py already contains the original
    # `if __name__ == "__main__": ...` dispatch (--test / chat loop)
    # verbatim, and it runs inside shared_globals where
    # __name__ == "__main__", so it fires automatically as part of the
    # exec below - no extra dispatch code needed here.
    _load_all()
