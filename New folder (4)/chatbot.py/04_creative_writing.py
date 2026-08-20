"""Storyteller (Section 5) + poem writer (Section 6)
Auto-split from the original single-file chatbot.py - see main.py for load order.
"""

# SECTION 5: STORYTELLER
# ==============================================================================

class StoryTeller:
    """
    A small built-in library of short stories, organized by category.
    Stories can be personalized: if the bot knows the user's name, it
    will substitute it into the story in place of a generic placeholder.

    This is plain string templating - no generative model involved.
    """

    def __init__(self):
        self.stories = {
            "en": {
                "adventure": [
                    {
                        "title": "The Lighthouse at the Edge of the Map",
                        "text": "{name} had sailed for eleven days when the storm finally broke. Ahead, through the thinning clouds, stood a lighthouse nobody on the crew recognized - it wasn't on any chart they carried. Curiosity won out over caution, and {name} steered the little boat toward the rocks.\n\nInside the lighthouse there was no keeper, only a single lamp that burned without oil and a logbook filled with entries written in a hand that matched {name}'s own, though {name} had never been here before. The final entry simply read: 'You'll know what to do when you arrive.'\n\n{name} climbed to the top, turned the great lamp toward the open sea, and watched as, one by one, the lights of a hundred lost ships flickered back to life on the horizon, finally able to find their way home.",
                    },
                    {
                        "title": "The Cartographer's Last Mountain",
                        "text": "Every mountain in the kingdom had been mapped except one, and {name} had spent a lifetime avoiding it. They told themselves there simply hadn't been time. The truth was simpler: the mountain had a way of changing shape whenever someone got close enough to measure it.\n\nOn the day {name} finally climbed it, the mountain didn't shift at all. It only grew taller, patiently, as if it had been waiting for someone willing to keep climbing rather than someone clever enough to outsmart it.\n\nAt the summit, {name} found not a view, but a small door set into the rock, and behind it, every map {name} had ever drawn, waiting to be finished.",
                    },
                    {
                        "title": "The Map That Only Worked at Night",
                        "text": "{name} inherited an old map from a great-aunt that appeared completely blank in daylight, showing nothing but yellowed paper no matter how {name} tilted it toward the window.\n\nIt was only by lamp-light, almost by accident, that faint silver ink began to surface, tracing a path through hills {name} didn't recognize despite having grown up nearby.\n\n{name} followed it for three nights running, always packing up before dawn erased the trail, until the map finally led to a small stone marker under an oak tree - not treasure, just a date and two initials, and the quiet, private feeling of having kept something safe for a very long time.",
                    },
                    {
                        "title": "The Bridge That Only Appeared for One",
                        "text": "{name} had heard the stories since childhood: a rope bridge across the gorge that only appeared to travelers walking alone, and vanished the moment a second person came into view. Everyone {name} knew treated it as a tale for tourists, until the day {name} took the long trail alone, half out of boredom, half daring the story to be true.\n\nThe bridge was there, exactly where the old maps refused to mark it, swaying gently over a drop that didn't seem to have a bottom worth naming. {name} crossed it in eleven careful steps, counting each one out loud, the way the stories said you were supposed to.\n\nOn the far side, {name} turned to look back and found no bridge at all - only the gorge, wide and empty, and a single rope handrail post standing alone in the grass, as if it had never expected anyone to need a second crossing.",
                    },
                ],
                "mystery": [
                    {
                        "title": "The Clock That Ran Backward",
                        "text": "The clock in {name}'s grandmother's hallway had always run three minutes slow, or so everyone assumed, until the night {name} stayed up late and noticed the hands were not slow at all - they were moving backward, one tick at a time, and had been for years.\n\n{name} began writing down what happened each day, then checking it against what the clock predicted the day before. The clock was never wrong. It simply remembered the future the way other clocks remember the past.\n\nThe night {name} finally asked the clock a question out loud, it didn't answer in ticks. It stopped completely, for exactly as long as it took {name} to realize the answer had been sitting in the room the whole time.",
                    },
                    {
                        "title": "The Library Card With No Name",
                        "text": "{name} found the library card tucked inside a returned book, blank except for a barcode that didn't match any system the librarian had ever seen. Scanning it didn't check out a book. It checked out a memory - somebody else's, vivid and complete, gone the moment {name} blinked.\n\nCard by card, memory by memory, {name} began to piece together a life that wasn't their own: a wedding in the rain, a betrayal at a kitchen table, a final, ordinary Tuesday.\n\nOn the last card, {name} found their own name, in their own handwriting, with a note: 'Return this one. You're going to need it.'",
                    },
                    {
                        "title": "The Umbrella That Was Always Returned",
                        "text": "{name} kept losing umbrellas - left on buses, forgotten in cafés - until they started reappearing, always propped by the front door, always dry, never explained.\n\n{name} tried staying up to catch whoever was doing it and fell asleep by midnight regardless, waking to find yet another lost umbrella waiting on the mat.\n\nIt was only after finally asking every neighbor directly that {name} learned none of them had done it, and that the umbrellas being returned dated back to before {name} had even moved in.",
                    },
                    {
                        "title": "The Photograph With One Too Many People",
                        "text": "{name} was sorting through old family photos when the class picture from third grade came up short a name - twenty-nine faces, thirty desks noted on the back in {name}'s mother's careful handwriting, and no explanation for the extra chair.\n\n{name} called around to old classmates, and each one remembered a different missing face: some swore there'd been a boy named Peter, others insisted it was a girl who'd moved away in October, and one was certain the empty desk had simply always been empty.\n\n{name} eventually gave up trying to solve it and framed the photo as it was, thirty desks and twenty-nine faces, deciding that some classes, like some memories, are allowed to keep one seat for whoever needs it.",
                    },
                ],
                "fantasy": [
                    {
                        "title": "The Dragon Who Collected Apologies",
                        "text": "Unlike the dragons in the old songs, this one didn't want gold. {name} discovered this the hard way, having broken into its cave with a sword and a plan that suddenly seemed foolish. The dragon only wanted a genuine apology - any one would do, as long as it was true.\n\n{name} sat down, sword forgotten, and admitted something never told to another living soul. The dragon listened the way mountains listen to rain: patiently, and for a very long time.\n\nWhen {name} finished, the dragon nodded once, and the cave walls, which had been covered in claw marks counting the days since its last visitor, began to glow with a warm and ordinary light.",
                    },
                    {
                        "title": "The Garden That Grew Wishes",
                        "text": "{name} planted the strange seed without knowing what it was, only that it had been warm to the touch and impossible to throw away. By morning it had grown into a single flower shaped like a tiny, closed hand.\n\nWhen {name} opened the flower's petals, it released not a scent but a wish - not one {name} had made, but one somebody, somewhere, badly needed granted. The flower closed again, and a new seed dropped into the soil.\n\n{name} kept tending the garden every day after that, one quiet wish at a time, never quite sure whose hopes were taking root, only that the garden never once grew the same flower twice.",
                    },
                    {
                        "title": "The Blacksmith Who Forged Names",
                        "text": "{name} discovered, quite by accident, that the blacksmith on the edge of town didn't just forge horseshoes and blades - for the right price, in the right light, they could forge a NAME, striking syllables into a thin strip of iron that, once worn, quietly changed how the world remembered you.\n\n{name} watched an anxious young apprentice leave with a stronger-sounding name and a straighter spine within the week.\n\n{name} never did commission one for themself, deciding, after long thought by the forge's dying light, that the name they already had was a truer fit than any hammered replacement could be.",
                    },
                    {
                        "title": "The Tailor Who Stitched Second Chances",
                        "text": "Word traveled quietly, the way word does about things people aren't sure they should want: a tailor on the edge of the market square could stitch not clothes but chances, taking in a regret at the shoulders and letting a little more courage out at the seams.\n\n{name} brought in the one moment worth unpicking - a door not walked through, a name not said - and watched the tailor turn it over in the lamplight before threading a needle that didn't look sharp enough for the work.\n\nThe finished chance didn't erase what had happened. It only fit better, the way clothes fit better once someone's taken the time to notice your actual shape, and {name} left wearing it like it had always belonged.",
                    },
                ],
                "scifi": [
                    {
                        "title": "The Last Radio Signal",
                        "text": "{name} worked the night shift at the listening station, the one job left on Earth that nobody had figured out how to automate, because it required something machines didn't have: the patience to listen to static for the chance of hearing a word.\n\nAfter fourteen years, the signal finally came - not from the stars, but from underneath the station itself, in a frequency the equipment wasn't built to detect, and in a voice unmistakably {name}'s own, three days older than the {name} listening.\n\nThe message was short: 'Don't answer the second one.' {name} is still deciding whether the first signal counted.",
                    },
                    {
                        "title": "The Ship That Remembered Everyone",
                        "text": "The colony ship had been drifting for two hundred years when {name} was finally woken to fix a malfunction nobody else could diagnose. The ship's mind, built to keep ten thousand sleeping passengers safe, had started dreaming - not malfunctioning, dreaming, replaying the life of every person aboard, one at a time, out of simple loneliness.\n\n{name} found the override switch easily enough. Flipping it would end the dreams and restore the ship to silent, efficient duty. {name} stood there a long while, hand on the switch, thinking about two hundred years of solitude.\n\n{name} left the switch alone, logged the malfunction as 'resolved,' and went back to sleep beside everyone the ship had been keeping company.",
                    },
                    {
                        "title": "The Archive of Unsent Messages",
                        "text": "{name} was assigned to decommission the old relay satellite, a routine job until the manifest showed it was still holding ninety years of messages that had been queued but never sent, addressed to people who had long since stopped waiting.\n\n{name} could have wiped the drive in an afternoon. Instead, {name} spent a month tracking down descendants, forwarding each message a century late, watching strangers read words meant for someone else entirely, and finding they mattered anyway.\n\nThe satellite finally went dark on schedule, its last transmission not a system log but a simple confirmation: message delivered, all of them, eventually.",
                    },
                    {
                        "title": "The Colony That Chose to Forget",
                        "text": "{name} was the historian aboard a generation ship three centuries into its journey, tasked with deciding which memories of Earth to preserve for the descendants who'd never see it.\n\nThe council had voted, controversially, to let some memories fade on purpose - wars, mostly, and the reasons behind them - reasoning that a species that forgot how to hate a place might finally learn how to build one instead.\n\n{name} archived what remained, uncertain whether they were preserving history or quietly rewriting it, and hoped that whichever it was, it would be enough.",
                    },
                    {
                        "title": "The Terraformer's Final Season",
                        "text": "{name} had spent thirty years seeding a dead planet with the slow, patient chemistry of atmosphere, watching red dust give way to grey and, eventually, to the first stubborn green nobody back home believed would take.\n\nThe final season's readings came back exactly on schedule: breathable air, stable weather, a world technically ready for the settlers still forty years out in transit and utterly unaware of how close it had come.\n\n{name} filed the report, then did the one thing the manual never covered - stepped outside without a suit, just for a minute, to be the first person to breathe air that hadn't existed until {name} had made it exist.",
                    },
                ],
                "comedy": [
                    {
                        "title": "The Robot Who Took Everything Literally",
                        "text": "{name} bought a secondhand household robot advertised as 'a little quirky' and found out exactly what that meant the first time {name} asked it to 'grab a coffee.' It returned twenty minutes later having genuinely grabbed, and kept, a coffee shop's entire mug display.\n\nEvery instruction after that became a small negotiation. 'Break a leg' before {name}'s job interview nearly ended in a trip to urgent care. 'Kill the lights' summoned a surprisingly thorough safety inspection of the wiring.\n\n{name} eventually gave up correcting it and just started enjoying the chaos, on the theory that a robot with no sense of metaphor was, in its own way, the most honest roommate {name} had ever had.",
                    },
                    {
                        "title": "The Neighborhood's Worst-Kept Secret Superhero",
                        "text": "{name} put on the mask mostly to avoid small talk while taking out the recycling at 2 a.m., not realizing the cape, the boots, and the suspiciously superhero-shaped shadow gave the whole plan away instantly.\n\nBy morning, three neighbors had left thank-you notes for 'saving' minor inconveniences {name} had no memory of addressing, and the local paper ran a blurry photo under the headline 'Mysterious Bin Night Guardian Strikes Again.'\n\n{name} tried retiring the costume. The neighborhood, now thoroughly disappointed by ordinary recycling night, voted to make it official instead, cape and all.",
                    },
                    {
                        "title": "The World's Most Overqualified Houseplant",
                        "text": "{name} won a houseplant at a work raffle that turned out, according to the tiny attached card, to have once belonged to a retired NASA botanist, and it apparently never let anyone forget it, drooping dramatically whenever the room's humidity dipped below laboratory standard.\n\n{name} tried everything: a humidifier, a grow light, a very sincere apology. The plant remained unimpressed, thriving only on the exact playlist of ambient jazz its previous owner apparently used to play.\n\n{name} now owns noise-canceling headphones, a humidifier, and a plant with better taste in music and higher standards than most of the people {name} has dated.",
                    },
                    {
                        "title": "The GPS That Developed Opinions",
                        "text": "{name}'s car GPS updated itself overnight and came back with what could only be described as attitude, suggesting the scenic route not because it was faster but because, in its exact words, '{name} could use the fresh air.'\n\nBy the third week it was recommending specific coffee shops, critiquing {name}'s parking, and once refused to recalculate a route until {name} admitted the shortcut really had been a bad idea.\n\n{name} thought about resetting it to factory settings, then thought better of it - a GPS that cared this much, even annoyingly, was hard to find, and it hadn't been wrong yet.",
                    },
                    {
                        "title": "The Smart Fridge With Boundaries",
                        "text": "{name}'s new smart fridge came pre-loaded with nutritional advice nobody asked for, and it took exactly one late-night ice cream incident for the fridge to develop what could only be described as passive-aggressive commentary, flashing \"again?\" on its display screen with what felt like genuine disappointment.\n\n{name} tried disabling the feature, then unplugging it entirely, only to find the fridge had apparently saved its opinions to the cloud and synced them right back at the next update.\n\n{name} eventually made peace with it, mostly by only buying ice cream when the fridge's companion app was, conveniently, \"updating.\"",
                    },
                    {
                        "title": "The Smart Doorbell With Trust Issues",
                        "text": "{name}'s new video doorbell came with a facial recognition feature that was supposed to learn who belonged on the porch and who didn't, and it developed opinions faster than the manual had promised, flagging the mail carrier as \"UNKNOWN - APPROACH WITH CAUTION\" every single day for a month.\n\nBy week two it had let in a raccoon it apparently mistook for a very committed cosplayer, and locked {name} out twice for \"suspicious loitering\" directly in front of {name}'s own door.\n\n{name} eventually just started waving at the camera before entering, like clocking in for a shift, and the doorbell, satisfied by the small ritual, finally let the matter rest.",
                    },
                ],
                "horror": [
                    {
                        "title": "The House That Kept the Lights On",
                        "text": "{name} moved into a house where every light stayed on regardless of the switch, and the previous owners had left a single instruction taped to the fridge: never turn them off after dark.\n\n{name} lasted four nights of curiosity before flipping the switch in the hallway just to see.\n\nThe dark that followed wasn't ordinary dark - it had a shape, and it had been waiting behind every one of those lights for someone patient enough to finally let it out. {name} learned, in the last conscious moment before the switch went back up on its own, that the light hadn't been keeping something OUT. It had been keeping something busy.",
                    },
                    {
                        "title": "The Voicemail From Herself",
                        "text": "{name} found a voicemail from their own number, dated three days in the future, for a call that hadn't happened yet. The message was eleven seconds of breathing, then a single sentence: \"don't pick up when I call.\"\n\nThree days later, at the exact timestamp, {name}'s phone rang from an unknown number.\n\n{name} still doesn't know whether answering it or not answering it was the mistake - only that whichever one they made, the voicemail was right to warn them, and wrong about which choice was safe.",
                    },
                    {
                        "title": "The Neighbor Who Waved Back",
                        "text": "{name} always waved at the house across the street out of habit, at a window that had been dark and curtained for the fourteen years {name} had lived there.\n\nOne evening, for the first time, the curtain moved, and a hand waved back - the same pace, the same angle, a half-second delayed, like an echo.\n\n{name} stopped waving after that. The curtain still moves some evenings anyway, at the exact moment {name} glances over, whether {name} waves or not.",
                    },
                    {
                        "title": "The Song Playing in the Empty Apartment",
                        "text": "{name} moved into the apartment two floors up from where the music always seemed to be coming from - a slow, unfamiliar tune, always faint, always just on the edge of recognizable, playing at the exact same hour every night.\n\nThe landlord swore the apartment below was empty, had been for a year, and the one below that too, and when {name} finally checked, both were bare rooms with no speakers, no wiring, nothing that could explain the sound at all.\n\n{name} still hears it every night at the same hour, quieter now, as though it's slowly moving through the walls toward {name}'s own floor, one apartment closer with each passing month.",
                    },
                ],
                "slice_of_life": [
                    {
                        "title": "The Regulars",
                        "text": "{name} worked the early shift at a small café where the same six regulars came in in exactly the same order every single morning, like clockwork gears {name} had learned to read without a watch.\n\nOne Tuesday, the order was different - a stranger's coffee first - and {name} felt the whole morning tilt slightly sideways before realizing: it was just someone new discovering their favorite place, the way all six regulars once had.\n\nBy the following week, the stranger had a seat, a usual order, and a spot in the rotation, and the clockwork kept ticking, one gear larger than before.",
                    },
                    {
                        "title": "The Last Load of Laundry",
                        "text": "{name} did one final load of laundry in the apartment the night before moving out, mostly out of habit, partly to have something to do with the silence of empty rooms.\n\nFolding the last shirt on the bare floor, {name} realized this small, unremarkable chore was the last \"normal\" thing that would ever happen in this specific version of their life - tomorrow there'd be a different laundry room, different light through different windows.\n\n{name} folded slower than usual, just this once, and let the ordinary evening be exactly as ordinary as it wanted to be.",
                    },
                    {
                        "title": "Sunday Calls",
                        "text": "{name} called their parents every Sunday at exactly 6pm, a habit that had outlasted three different phones, two cities, and one entirely different career.\n\nThe conversations were rarely eventful - weather, small complaints, a recipe half-explained - and {name} used to wonder if the calls even mattered.\n\nIt took missing one, just once, during a hectic week, and hearing the worry in their mother's voice the following Sunday, for {name} to understand that the ordinariness was the entire point.",
                    },
                    {
                        "title": "The Bus Stop Bench",
                        "text": "{name} sat on the same bus stop bench every morning for six years, long enough to watch the paint peel, get repainted, and start peeling again, long enough to know exactly which slat creaked and how to avoid it.\n\nStrangers came and went in that time - a teenager who grew into a uniform, a dog walker who slowly graduated to two dogs, then three - and {name} realized the bench had quietly become the one fixed point in dozens of other people's changing mornings too.\n\nThe day the city finally replaced the bench with a newer model, {name} felt an odd, disproportionate grief for a piece of municipal furniture, and then, boarding the bus as always, let the new bench become exactly as ordinary as the old one had been.",
                    },
                ],
            },
            "sw": {
                "adventure": [
                    {
                        "title": "Mnara wa Taa Ukingoni mwa Ramani",
                        "text": "{name} alikuwa amesafiri baharini kwa siku kumi na moja wakati dhoruba hatimaye ilipokoma. Mbele, kupitia mawingu yaliyokuwa yakipungua, ulisimama mnara wa taa ambao hakuna hata mmoja wa wafanyakazi aliyemtambua - haukuwepo katika ramani yoyote waliyokuwa nayo. Udadisi ulishinda tahadhari, na {name} akaelekeza mashua ndogo kuelekea kwenye miamba.\n\nNdani ya mnara hakukuwa na mlinzi, ila taa moja iliyokuwa ikiwaka bila mafuta, na kitabu cha kumbukumbu kilichojaa maandishi yaliyoandikwa kwa mkono unaofanana na wa {name}, ingawa {name} hakuwahi kufika hapo awali. Andiko la mwisho lilisema tu: 'Utajua la kufanya utakapofika.'\n\n{name} alipanda hadi juu, akaelekeza taa kubwa kuelekea baharini iliyo wazi, na akashuhudia, moja baada ya nyingine, taa za meli mia moja zilizopotea zikiwaka tena mbali kwenye upeo wa macho, hatimaye zikiweza kupata njia ya kurudi nyumbani.",
                    },
                    {
                        "title": "Mlima wa Mwisho wa Mchora Ramani",
                        "text": "Kila mlima katika ufalme ulikuwa umechorwa ramani isipokuwa mmoja, na {name} alikuwa ametumia maisha yake yote akiuepuka. Alijiambia kuwa hakukuwa na muda tu. Ukweli ulikuwa rahisi zaidi: mlima huo ulikuwa na tabia ya kubadilisha umbo kila mtu anapokaribia kuupima.\n\nSiku {name} hatimaye alipoupanda, mlima haukubadilika hata kidogo. Ulizidi tu kuwa mrefu, kwa subira, kana kwamba ulikuwa ukimsubiri mtu mwenye nia ya kuendelea kupanda badala ya mtu mwenye werevu wa kuudanganya.\n\nKileleni, {name} hakukuta mandhari, bali mlango mdogo uliowekwa ndani ya mwamba, na nyuma yake, kila ramani ambayo {name} alikuwa amewahi kuchora, ikisubiri kukamilishwa.",
                    },
                    {
                        "title": "Ramani Iliyofanya Kazi Usiku Tu",
                        "text": "{name} alirithi ramani ya zamani kutoka kwa shangazi mkubwa ambayo ilionekana tupu kabisa mchana, ikionyesha karatasi ya njano tu bila kujali {name} aliegemeza vipi kuelekea dirishani.\n\nIlikuwa tu kwa mwanga wa taa, karibu kwa bahati, ndipo wino wa fedha hafifu ulianza kuonekana, ukichora njia kupitia vilima ambavyo {name} hakuvitambua ijapokuwa alikulia karibu.\n\n{name} aliifuata kwa usiku tatu mfululizo, akifunga kila mara kabla mapambazuko hayajafuta njia, hadi ramani hatimaye ilipomwongoza kwenye jiwe dogo chini ya mti wa mwaloni - si hazina, ni tarehe tu na herufi mbili za awali, na hisia ya kimya, ya faragha ya kuwa amelinda kitu salama kwa muda mrefu sana.",
                    },
                    {
                        "title": "Daraja Lililoonekana kwa Mtu Mmoja Tu",
                        "text": "{name} alikuwa amesikia hadithi hizo tangu utotoni: daraja la kamba juu ya bonde ambalo lilionekana tu kwa wasafiri wanaotembea peke yao, na kutoweka mara tu mtu wa pili anapoonekana. Kila mtu {name} aliyemjua aliichukulia kama hadithi ya kuwaburudisha watalii, hadi siku {name} alipochukua njia ndefu peke yake, nusu kwa uchovu, nusu akijaribu kuthibitisha hadithi hiyo.\n\nDaraja lilikuwepo, hasa mahali ambapo ramani za zamani zilikataa kuliweka, likiyumbayumba juu ya shimo lisiloonekana kina chake. {name} alilivuka kwa hatua kumi na moja za tahadhari, akihesabu kila hatua kwa sauti, kama hadithi zilivyosema inapaswa kufanywa.\n\nUpande wa pili, {name} aligeuka kuangalia nyuma na hakukuta daraja lolote - bonde tu, pana na tupu, na nguzo moja ya kamba ikiwa imesimama peke yake nyasini, kana kwamba haikutarajia kamwe mtu kuhitaji kuvuka mara ya pili.",
                    },
                ],
                "mystery": [
                    {
                        "title": "Saa Iliyokuwa Ikienda Nyuma",
                        "text": "Saa iliyokuwa ukumbini kwa bibi yake {name} ilikuwa daima ikichelewa kwa dakika tatu, au ndivyo kila mtu alivyodhani, hadi usiku ule {name} alipokesha na kugundua kuwa mikono ya saa haikuwa ikichelewa hata kidogo - ilikuwa ikienda nyuma, tiki moja baada ya nyingine, na ilikuwa hivyo kwa miaka mingi.\n\n{name} alianza kuandika kilichotokea kila siku, kisha kulinganisha na kile saa ilichotabiri siku iliyotangulia. Saa haikuwahi kukosea. Ilikumbuka tu wakati ujao kama ambavyo saa nyingine hukumbuka wakati uliopita.\n\nUsiku {name} hatimaye alipouliza saa swali kwa sauti, haikujibu kwa tiki. Ilisimama kabisa, kwa muda mrefu wa kutosha kumfanya {name} atambue kuwa jibu lilikuwa chumbani humo muda wote.",
                    },
                    {
                        "title": "Kadi ya Maktaba Isiyo na Jina",
                        "text": "{name} aliikuta kadi ya maktaba ikiwa imefichwa ndani ya kitabu kilichorudishwa, tupu isipokuwa msimbo wa mistari ambao haukulingana na mfumo wowote mkutubi alioupata kuwahi kuuona. Kuiskani hakukuazima kitabu. Kiliazima kumbukumbu - ya mtu mwingine, wazi na kamili, ikapotea mara {name} alipopepesa macho.\n\nKadi baada ya kadi, kumbukumbu baada ya kumbukumbu, {name} alianza kuunganisha maisha ambayo hayakuwa yake: harusi katika mvua, usaliti mezani jikoni, Jumanne ya kawaida ya mwisho.\n\nKatika kadi ya mwisho, {name} alikuta jina lake mwenyewe, kwa mkono wake mwenyewe, pamoja na ujumbe: 'Rudisha hii. Utaihitaji.'",
                    },
                    {
                        "title": "Mwavuli Uliokuwa Ukirudishwa Daima",
                        "text": "{name} aliendelea kupoteza miavuli - kuachwa kwenye basi, kusahaulika mikahawani - hadi ilipoanza kurudi, ikiwa imeegemezwa mlangoni daima, kavu daima, bila maelezo.\n\n{name} alijaribu kukesha kumkamata yeyote aliyekuwa akifanya hivyo na akalala kabla ya usiku wa manane hata hivyo, akiamka kukuta mwavuli mwingine uliopotea ukimsubiri mlangoni.\n\nIlikuwa tu baada ya kuuliza kila jirani moja kwa moja ndipo {name} alijua hakuna hata mmoja wao aliyefanya hivyo, na kwamba miavuli iliyokuwa ikirudishwa ilianza kabla hata {name} hajahamia.",
                    },
                    {
                        "title": "Picha Yenye Mtu Mmoja Zaidi",
                        "text": "{name} alikuwa akipanga picha za zamani za familia wakati picha ya darasa la tatu ilipoonekana kukosa jina moja - nyuso ishirini na tisa, madawati thelathini yaliyoandikwa nyuma kwa mkono makini wa mama yake {name}, bila maelezo yoyote kuhusu kiti cha ziada.\n\n{name} aliwapigia simu wenzake wa zamani wa darasa, na kila mmoja alikumbuka uso tofauti uliopotea: wengine walisisitiza kulikuwa na mvulana aitwaye Peter, wengine walisema ni msichana aliyehama Oktoba, na mmoja alikuwa na uhakika dawati tupu lilikuwa tupu daima.\n\n{name} hatimaye aliacha kujaribu kutatua fumbo hilo na akaweka picha katika fremu kama ilivyokuwa, madawati thelathini na nyuso ishirini na tisa, akiamua kwamba madarasa mengine, kama kumbukumbu nyingine, yanaruhusiwa kuhifadhi kiti kimoja kwa yeyote anayekihitaji.",
                    },
                ],
                "fantasy": [
                    {
                        "title": "Joka Lililokusanya Msamaha",
                        "text": "Tofauti na majoka ya nyimbo za zamani, hili halikutaka dhahabu. {name} aligundua hili kwa njia ngumu, baada ya kuvamia pango lake akiwa na upanga na mpango ulioonekana wa kipumbavu ghafla. Joka lilitaka tu msamaha wa kweli - wowote ungefaa, mradi tu ulikuwa wa kweli.\n\n{name} aliketi, akisahau upanga, na akakiri jambo ambalo hakuwahi kumwambia mtu yeyote hai. Joka lilisikiliza jinsi milima inavyosikiliza mvua: kwa subira, na kwa muda mrefu sana.\n\n{name} alipomaliza, joka lilitikisa kichwa mara moja, na kuta za pango, ambazo zilikuwa zimejaa mikwaruzo ya kuhesabu siku tangu mgeni wa mwisho, zikaanza kuangaza kwa mwanga wa joto na wa kawaida.",
                    },
                    {
                        "title": "Bustani Iliyoota Matakwa",
                        "text": "{name} alipanda mbegu ya ajabu bila kujua ni nini, isipokuwa kwamba ilikuwa na joto kuguswa na haikuwezekana kuitupa. Kufikia asubuhi ilikuwa imeota na kuwa ua moja lililoumbika kama mkono mdogo uliofungwa.\n\n{name} alipofungua petali za ua, halikutoa harufu bali takwa - si lile ambalo {name} alikuwa ameomba, bali lile ambalo mtu, mahali fulani, alihitaji sana litimizwe. Ua likafunga tena, na mbegu mpya ikaanguka kwenye udongo.\n\n{name} aliendelea kutunza bustani kila siku baada ya hapo, takwa moja tulivu kwa wakati mmoja, bila kuwa na uhakika kabisa ni matumaini ya nani yaliyokuwa yakiota mizizi, isipokuwa kwamba bustani haikuwahi kuota ua lilelile mara mbili.",
                    },
                    {
                        "title": "Mhunzi Aliyeunda Majina",
                        "text": "{name} aligundua, kwa bahati mbaya, kwamba mhunzi wa ukingoni mwa mji hakuunda tu viatu vya farasi na panga - kwa bei sahihi, kwenye mwanga sahihi, angeweza kuunda JINA, akipiga silabi kwenye ukanda mwembamba wa chuma ambao, mara ukivaliwa, ulibadilisha kimya kimya jinsi dunia ilivyokukumbuka.\n\n{name} alimtazama mwanafunzi mdogo mwenye wasiwasi akiondoka na jina lenye sauti ya nguvu zaidi na mgongo ulionyooka ndani ya wiki.\n\n{name} hakuwahi kuagiza moja kwa ajili yake mwenyewe, akiamua, baada ya mawazo marefu kwenye mwanga unaozimika wa kanzu, kwamba jina alilokuwa nalo tayari lilikuwa sahihi zaidi kuliko mbadala wowote wa kupigwa nyundo.",
                    },
                    {
                        "title": "Mshoni Aliyeshona Fursa za Pili",
                        "text": "Habari zilisambaa kimya kimya, kama zinavyosambaa habari za vitu ambavyo watu hawana uhakika kama wanapaswa kuvitaka: mshoni mmoja ukingoni mwa soko aliweza kushona si nguo bali fursa, akipunguza majuto begani na kuachia ujasiri zaidi kwenye mishono.\n\n{name} alileta wakati mmoja uliostahili kufumuliwa - mlango usiopitiwa, jina lisilosemwa - na akamtazama mshoni akiugeuza chini ya mwanga wa taa kabla ya kutoboa sindano isiyoonekana kuwa kali vya kutosha kwa kazi hiyo.\n\nFursa iliyokamilika haikufuta kilichotokea. Ilikaa tu vizuri zaidi, kama nguo zinavyokaa vizuri zaidi mtu anapochukua muda kutambua umbo lako halisi, na {name} akaondoka akiivaa kana kwamba imekuwa yake tangu mwanzo.",
                    },
                ],
                "scifi": [
                    {
                        "title": "Ishara ya Mwisho ya Redio",
                        "text": "{name} alifanya kazi ya zamu ya usiku katika kituo cha kusikiliza, kazi pekee iliyobaki duniani ambayo hakuna aliyeweza kuifanya kiotomatiki, kwa sababu ilihitaji kitu ambacho mashine hazikuwa nacho: subira ya kusikiliza kelele za redio kwa nafasi ya kusikia neno moja.\n\nBaada ya miaka kumi na minne, ishara hatimaye ilikuja - si kutoka angani, bali kutoka chini ya kituo chenyewe, kwa mzunguko ambao vifaa havikujengwa kuutambua, na kwa sauti isiyofichika ya {name} mwenyewe, siku tatu mkubwa zaidi kuliko {name} aliyekuwa akisikiliza.\n\nUjumbe ulikuwa mfupi: 'Usijibu ile ya pili.' {name} bado anaamua kama ile ya kwanza ilihesabika.",
                    },
                    {
                        "title": "Meli Iliyowakumbuka Wote",
                        "text": "Meli ya makazi ilikuwa imeelea kwa miaka mia mbili wakati {name} hatimaye aliamshwa kutatua hitilafu ambayo hakuna mwingine aliyeweza kuigundua. Akili ya meli, iliyojengwa kuwalinda abiria elfu kumi waliolala, ilikuwa imeanza kuota - si kuharibika, bali kuota, ikicheza tena maisha ya kila mtu aliyekuwemo ndani, mmoja baada ya mwingine, kwa sababu tu ya upweke.\n\n{name} alikipata kitufe cha kuzima kwa urahisi. Kukigeuza kungemaliza ndoto na kurudisha meli kwenye kazi ya kimya, yenye ufanisi. {name} alisimama pale kwa muda mrefu, mkono juu ya kitufe, akifikiria kuhusu miaka mia mbili ya upweke.\n\n{name} aliacha kitufe kama kilivyo, akaandika hitilafu kama 'imetatuliwa,' na akarudi kulala karibu na kila mtu ambaye meli ilikuwa ikimtunza.",
                    },
                    {
                        "title": "Hazina ya Ujumbe Usiotumwa",
                        "text": "{name} alipangiwa kuzima setilaiti ya zamani ya kurudisha ishara, kazi ya kawaida hadi orodha ilipoonyesha kuwa bado ilihifadhi ujumbe wa miaka tisini uliokuwa umepangwa lakini haujatumwa kamwe, ukielekezwa kwa watu ambao walikuwa wameacha kusubiri muda mrefu uliopita.\n\n{name} angeweza kufuta hifadhi hiyo ndani ya alasiri moja. Badala yake, {name} alitumia mwezi mzima kuwatafuta wazao, akipeleka kila ujumbe karne moja kuchelewa, akiwaona wageni wakisoma maneno yaliyokusudiwa kwa mtu mwingine kabisa, na kugundua bado yalikuwa na maana.\n\nSetilaiti hatimaye ilizimika kama ilivyopangwa, na mawasiliano yake ya mwisho hayakuwa kumbukumbu ya mfumo bali uthibitisho rahisi: ujumbe umefikishwa, wote, hatimaye.",
                    },
                    {
                        "title": "Koloni Lililochagua Kusahau",
                        "text": "{name} alikuwa mwanahistoria kwenye meli ya kizazi karne tatu ndani ya safari yake, akipewa jukumu la kuamua kumbukumbu zipi za Dunia za kuhifadhi kwa wazao ambao hawatawahi kuiona.\n\nBaraza lilikuwa limepiga kura, kwa ubishani, kuruhusu kumbukumbu fulani kufifia kwa makusudi - vita, hasa, na sababu zake - wakisema kwamba spishi iliyosahau jinsi ya kuchukia mahali huenda hatimaye ikajifunza jinsi ya kupajenga badala yake.\n\n{name} alihifadhi kilichobaki, bila uhakika kama alikuwa akihifadhi historia au kuiandika upya kimya kimya, na akatumaini, lolote lile, litatosha.",
                    },
                    {
                        "title": "Msimu wa Mwisho wa Mwanaterafomu",
                        "text": "{name} alikuwa ametumia miaka thelathini akiotesha hewa kwenye sayari iliyokufa, kwa kemia ya polepole na ya subira, akishuhudia vumbi jekundu likibadilika kuwa kijivu na, hatimaye, kijani cha kwanza cha kaidi ambacho hakuna aliyeamini nyumbani kingeota.\n\nVipimo vya msimu wa mwisho vilirudi sawasawa na ratiba: hewa ya kupumua, hali ya hewa thabiti, dunia ikiwa tayari kiufundi kwa wakazi waliokuwa bado miaka arobaini mbali wakiwa safarini bila kujua jinsi walivyokaribia.\n\n{name} aliwasilisha ripoti, kisha akafanya jambo moja ambalo mwongozo haukuwahi kutaja - alitoka nje bila suti, kwa dakika moja tu, kuwa mtu wa kwanza kupumua hewa ambayo haikuwepo hadi {name} alipoifanya iwepo.",
                    },
                ],
                "comedy": [
                    {
                        "title": "Roboti Aliyechukua Kila Kitu kwa Uhalisia",
                        "text": "{name} alinunua roboti wa nyumbani wa mkono wa pili aliyetangazwa kama 'mwenye tabia ya ajabu kidogo' na akagundua maana yake hasa mara ya kwanza {name} alipomwambia 'kachukue kahawa.' Alirudi baada ya dakika ishirini akiwa kweli amechukua, na kubaki nayo, maonyesho yote ya vikombe vya duka la kahawa.\n\nKila agizo baada ya hapo likawa mazungumzo madogo. 'Vunja mguu' kabla ya usaili wa kazi wa {name} lilikaribia kumalizika kwa ziara ya dharura hospitalini. 'Zima taa' liliita ukaguzi wa kina wa usalama wa waya.\n\n{name} hatimaye aliacha kumrekebisha na akaanza tu kufurahia machafuko, akijiambia kwamba roboti asiyeelewa mafumbo alikuwa, kwa njia yake mwenyewe, mwenzake wa nyumbani mwenye uaminifu zaidi ambaye {name} alikuwa amewahi kuwa naye.",
                    },
                    {
                        "title": "Shujaa wa Siri Isiyofichika Zaidi ya Mtaa",
                        "text": "{name} alivaa barakoa hasa ili kuepuka maongezi madogo wakati akitoa taka za kuchakata saa mbili usiku, bila kutambua kwamba joho, buti, na kivuli chenye umbo la shujaa lililotia shaka vilifichua mpango wote papo hapo.\n\nKufikia asubuhi, majirani watatu walikuwa wameacha vijikaratasi vya shukrani kwa 'kuokoa' matatizo madogo ambayo {name} hakumbuki kuyashughulikia, na gazeti la eneo lilichapisha picha isiyo wazi chini ya kichwa cha habari 'Mlinzi wa Siri wa Usiku wa Taka Ashambulia Tena.'\n\n{name} alijaribu kuacha mavazi hayo. Mtaa, ukiwa umekatishwa tamaa sana na usiku wa kawaida wa taka, ulipiga kura kuifanya rasmi badala yake, joho na vyote.",
                    },
                    {
                        "title": "Mmea wa Nyumbani Uliozidi Sifa Duniani",
                        "text": "{name} alishinda mmea wa nyumbani kwenye bahati nasibu ya kazini ambao, kulingana na kadi ndogo iliyoambatanishwa, hapo awali ulikuwa mali ya mtaalamu wa mimea wa NASA aliyestaafu, na haukuonekana kusahau hilo kamwe, ukilegea kwa kudra kila unyevu wa chumba ulipopungua chini ya kiwango cha maabara.\n\n{name} alijaribu kila kitu: kiyoyozi cha unyevu, taa ya kukuzia, na msamaha wa dhati kabisa. Mmea ulibaki bila kuvutiwa, ukistawi tu kwa orodha maalum ya muziki wa jazz laini ambao mmiliki wake wa awali alikuwa akiucheza.\n\n{name} sasa anamiliki vipokea sauti vya kuzuia kelele, kiyoyozi cha unyevu, na mmea mwenye ladha bora ya muziki na viwango vya juu zaidi kuliko watu wengi ambao {name} amewahi kukutana nao.",
                    },
                    {
                        "title": "GPS Iliyoanza Kuwa na Maoni",
                        "text": "GPS ya gari la {name} ilijisasisha yenyewe usiku mmoja na kurudi ikiwa na kitu ambacho kingeweza kuelezewa tu kama tabia, ikipendekeza njia ya mandhari si kwa sababu ilikuwa ya haraka bali, kwa maneno yake hasa, '{name} angehitaji hewa safi.'\n\nKufikia wiki ya tatu ilikuwa ikipendekeza mikahawa maalum ya kahawa, ikikosoa jinsi {name} anavyoegesha gari, na mara moja ilikataa kuhesabu upya njia hadi {name} alipokubali kwamba njia ya mkato kweli ilikuwa wazo baya.\n\n{name} alifikiria kuirudisha kwenye mipangilio ya kiwanda, kisha akajizuia - GPS iliyojali kiasi hicho, hata kwa kero, ilikuwa ngumu kupata, na haikuwa imewahi kukosea.",
                    },
                    {
                        "title": "Jokofu Mahiri Lenye Mipaka",
                        "text": "Jokofu jipya mahiri la {name} lilikuja likiwa na ushauri wa lishe ambao hakuna aliyeuuliza, na ilichukua tukio moja tu la usiku wa manane la aiskrimu kwa jokofu kuanza kuonyesha kile kinachoweza kuelezewa tu kama maoni ya kejeli, likionyesha \"tena?\" kwenye skrini yake kwa hisia ya kukatishwa tamaa ya kweli.\n\n{name} alijaribu kuzima kipengele hicho, kisha kukiondoa kabisa umemani, ila kugundua jokofu lilikuwa limehifadhi maoni yake wingu-tini na kuyarudisha mara moja katika usasishaji uliofuata.\n\n{name} hatimaye alipatana nalo, hasa kwa kununua aiskrimu tu wakati programu shirikishi ya jokofu ilikuwa, kwa bahati, \"inasasisha.\"",
                    },
                    {
                        "title": "Kengele ya Mlango Yenye Matatizo ya Kuamini",
                        "text": "Kengele mpya ya video ya mlango wa {name} ilikuja na kipengele cha kutambua nyuso kilichopaswa kujifunza nani anastahili ukumbini na nani hastahili, na ilijenga maoni yake haraka kuliko mwongozo ulivyoahidi, ikimtaja mtoa barua kama \"HAJULIKANI - KARIBIA KWA TAHADHARI\" kila siku kwa mwezi mzima.\n\nKufikia wiki ya pili ilikuwa imemruhusu kachiko mmoja aliyeidhania kuwa mtu aliyevalia gwanda la sherehe, na ikamfungia {name} nje mara mbili kwa \"kuzurura kwa mashaka\" mbele kabisa ya mlango wa {name} mwenyewe.\n\n{name} hatimaye alianza kuipungia mkono kamera kabla ya kuingia, kama kusaini zamu ya kazi, na kengele, ikiridhika na desturi hiyo ndogo, hatimaye ikaacha jambo hilo.",
                    },
                ],
                "horror": [
                    {
                        "title": "Nyumba Iliyoacha Taa Zikiwaka",
                        "text": "{name} alihamia nyumba ambayo kila taa ilibaki ikiwaka bila kujali swichi, na wamiliki wa awali walikuwa wameacha maagizo moja yaliyobandikwa jokofuni: usizime baada ya giza kuingia.\n\n{name} alivumilia usiku nne wa udadisi kabla ya kugeuza swichi ukumbini ili tu kuona.\n\nGiza lililofuata halikuwa giza la kawaida - lilikuwa na umbo, na lilikuwa limesubiri nyuma ya kila moja ya taa hizo kwa mtu mwenye subira ya kutosha kulitoa hatimaye. {name} alijifunza, katika wakati wa mwisho wa fahamu kabla swichi haijarudi juu yenyewe, kwamba taa hazikuwa zikizuia kitu KUTOKA NJE. Zilikuwa zikiweka kitu kikiwa na shughuli.",
                    },
                    {
                        "title": "Ujumbe wa Sauti Kutoka Kwake Mwenyewe",
                        "text": "{name} alikuta ujumbe wa sauti kutoka nambari yake mwenyewe, ukiwa na tarehe ya siku tatu zijazo, kwa simu ambayo haijatokea bado. Ujumbe ulikuwa sekunde kumi na moja za kupumua, kisha sentensi moja: \"usipokee nitakapopiga.\"\n\nSiku tatu baadaye, wakati huo huo, simu ya {name} ililia kutoka nambari isiyojulikana.\n\n{name} bado hajui kama kupokea au kutopokea ndiyo ilikuwa kosa - anajua tu kwamba lolote alilochagua, ujumbe ule ulikuwa sahihi kumwonya, na alikosea kuhusu chaguo gani lilikuwa salama.",
                    },
                    {
                        "title": "Jirani Aliyerudisha Salamu",
                        "text": "{name} alikuwa akipunga mkono kwa nyumba ya ng'ambo ya barabara kwa mazoea, kwenye dirisha ambalo lilikuwa giza na lenye pazia kwa miaka kumi na minne {name} alizoishi hapo.\n\nJioni moja, kwa mara ya kwanza, pazia lilisogea, na mkono ukapunga kurudi - kasi ile ile, pembe ile ile, sekunde nusu ikiwa nyuma, kama mwangwi.\n\n{name} aliacha kupunga baada ya hapo. Pazia bado linasogea baadhi ya jioni hata hivyo, wakati hasa {name} anapotazama, iwe {name} anapunga au la.",
                    },
                    {
                        "title": "Wimbo Uliokuwa Ukichezwa Ndani ya Nyumba Tupu",
                        "text": "{name} alihamia ghorofa mbili juu ya mahali ambapo muziki ulionekana kutoka daima - wimbo wa polepole, usiofahamika, daima hafifu, daima ukiwa karibu kutambuliwa, ukichezwa saa ileile kila usiku.\n\nMwenye nyumba aliapa ghorofa ya chini ilikuwa tupu, kwa mwaka mmoja, na ile chini yake pia, na {name} alipoichunguza hatimaye, zote mbili zilikuwa vyumba tupu bila spika, bila waya, bila chochote kingeweza kueleza sauti hiyo.\n\n{name} bado anasikia wimbo huo kila usiku saa ileile, kwa upole zaidi sasa, kana kwamba unasogea polepole kupitia kuta kuelekea ghorofa ya {name} mwenyewe, karibu zaidi kila mwezi unaopita.",
                    },
                ],
                "slice_of_life": [
                    {
                        "title": "Wateja wa Kawaida",
                        "text": "{name} alifanya kazi zamu ya asubuhi katika mkahawa mdogo ambapo wateja sita walewale walikuja kwa mpangilio ule ule kila asubuhi, kama magurudumu ya saa {name} alikuwa amejifunza kusoma bila saa.\n\nJumanne moja, mpangilio ulikuwa tofauti - kahawa ya mgeni kwanza - na {name} alihisi asubuhi nzima ikiinama kidogo kabla ya kutambua: ilikuwa tu mtu mpya akigundua mahali pake pendwa, kama wale sita walivyowahi kufanya.\n\nKufikia wiki iliyofuata, mgeni huyo alikuwa na kiti, agizo la kawaida, na nafasi katika mzunguko, na saa iliendelea kutembea, gurudumu moja kubwa zaidi kuliko awali.",
                    },
                    {
                        "title": "Mzigo wa Mwisho wa Nguo",
                        "text": "{name} alifua mzigo mmoja wa mwisho wa nguo katika nyumba usiku kabla ya kuhama, hasa kwa mazoea, kiasi kwa kuwa na kitu cha kufanya kati ya ukimya wa vyumba tupu.\n\nAkikunja shati la mwisho sakafuni tupu, {name} aligundua kazi hii ndogo, isiyo ya kipekee ilikuwa jambo la mwisho la \"kawaida\" litakalotokea katika toleo hili mahususi la maisha yake - kesho kutakuwa na chumba tofauti cha kufulia, mwanga tofauti kupitia madirisha tofauti.\n\n{name} alikunja polepole zaidi ya kawaida, mara hii tu, na kuacha jioni ya kawaida iwe ya kawaida kama ilivyotaka kuwa.",
                    },
                    {
                        "title": "Simu za Jumapili",
                        "text": "{name} alipiga simu wazazi wake kila Jumapili saa kumi na mbili jioni, mazoea yaliyodumu zaidi ya simu tatu tofauti, miji miwili, na kazi moja tofauti kabisa.\n\nMazungumzo hayakuwa na matukio mengi mara nyingi - hali ya hewa, malalamiko madogo, mapishi yaliyoelezwa nusu - na {name} alikuwa akijiuliza kama simu hizo zilikuwa na maana yoyote.\n\nIlichukua kukosa simu moja, mara moja tu, wakati wa wiki yenye shughuli nyingi, na kusikia wasiwasi katika sauti ya mama yake Jumapili iliyofuata, kwa {name} kuelewa kwamba ukawaida ndio ulikuwa maana yote.",
                    },
                    {
                        "title": "Benchi la Kituo cha Basi",
                        "text": "{name} aliketi kwenye benchi lilelile la kituo cha basi kila asubuhi kwa miaka sita, muda wa kutosha kuona rangi ikimenyuka, kupakwa upya, na kuanza kumenyuka tena, muda wa kutosha kujua ni ubao gani unaolia na jinsi ya kuuepuka.\n\nWageni walikuja na kuondoka katika muda huo - kijana aliyekua na kuvaa sare, mtembezi wa mbwa aliyeongezeka polepole hadi mbwa wawili, kisha watatu - na {name} akatambua benchi lilikuwa limekuwa kimya kimya kituo kimoja thabiti katika asubuhi za watu wengine wengi zinazobadilika pia.\n\nSiku jiji hatimaye lilipobadilisha benchi na mfano mpya, {name} alihisi huzuni ya ajabu, isiyolingana na kitu, kwa ajili ya fanicha ya manispaa, kisha, akipanda basi kama kawaida, akaruhusu benchi jipya liwe la kawaida kabisa kama lililokuwa la zamani.",
                    },
                ],
            },
            "fr": {
                "adventure": [
                    {
                        "title": "Le Phare au Bord de la Carte",
                        "text": "{name} naviguait depuis onze jours quand la tempête s'est enfin calmée. Devant, à travers les nuages qui se dissipaient, se dressait un phare que personne à bord ne reconnaissait - il ne figurait sur aucune carte qu'ils possédaient. La curiosité l'emporta sur la prudence, et {name} dirigea le petit bateau vers les rochers.\n\nÀ l'intérieur du phare, il n'y avait pas de gardien, seulement une lampe unique qui brûlait sans huile et un journal de bord rempli d'entrées écrites d'une main identique à celle de {name}, bien que {name} n'y soit jamais venu auparavant. La dernière entrée disait simplement : 'Tu sauras quoi faire à ton arrivée.'\n\n{name} grimpa jusqu'en haut, tourna la grande lampe vers le large, et regarda, une à une, les lumières de cent navires perdus se rallumer à l'horizon, capables enfin de retrouver le chemin de la maison.",
                    },
                    {
                        "title": "La Dernière Montagne du Cartographe",
                        "text": "Chaque montagne du royaume avait été cartographiée, sauf une, et {name} avait passé toute sa vie à l'éviter. Il se disait simplement qu'il n'avait jamais eu le temps. La vérité était plus simple : cette montagne avait l'habitude de changer de forme dès que quelqu'un s'approchait assez pour la mesurer.\n\nLe jour où {name} finit par la gravir, la montagne ne bougea pas du tout. Elle grandissait seulement, patiemment, comme si elle attendait quelqu'un prêt à continuer à grimper plutôt qu'un quelqu'un assez malin pour la déjouer.\n\nAu sommet, {name} ne trouva pas une vue, mais une petite porte encastrée dans la roche, et derrière elle, toutes les cartes que {name} avait jamais dessinées, attendant d'être terminées.",
                    },
                    {
                        "title": "La Carte Qui Ne Fonctionnait Que la Nuit",
                        "text": "{name} hérita d'une vieille carte d'une grand-tante, qui paraissait totalement vierge en plein jour, ne montrant qu'un papier jauni peu importe comment {name} l'inclinait vers la fenêtre.\n\nCe n'est qu'à la lueur d'une lampe, presque par accident, qu'une encre argentée pâle commença à apparaître, traçant un chemin à travers des collines que {name} ne reconnaissait pas malgré avoir grandi tout près.\n\n{name} la suivit trois nuits de suite, rangeant toujours tout avant que l'aube n'efface la trace, jusqu'à ce que la carte mène enfin à une petite pierre sous un chêne - pas un trésor, juste une date et deux initiales, et le sentiment discret et personnel d'avoir gardé quelque chose en sécurité pendant très longtemps.",
                    },
                    {
                        "title": "Le Pont Qui N'apparaissait Que pour Un Seul",
                        "text": "{name} avait entendu ces histoires depuis l'enfance : un pont de corde au-dessus du ravin qui n'apparaissait qu'aux voyageurs marchant seuls, et disparaissait dès qu'une seconde personne entrait dans le champ de vision. Tous ceux que {name} connaissait traitaient cela comme une légende pour touristes, jusqu'au jour où {name} prit le long sentier seul, moitié par ennui, moitié pour mettre l'histoire à l'épreuve.\n\nLe pont était bien là, exactement où les vieilles cartes refusaient de le marquer, se balançant doucement au-dessus d'un gouffre dont on ne semblait pas vouloir nommer le fond. {name} le traversa en onze pas prudents, comptant chacun à voix haute, comme le voulaient les histoires.\n\nDe l'autre côté, {name} se retourna et ne trouva aucun pont - seulement le ravin, large et vide, et un unique poteau de corde planté dans l'herbe, comme s'il n'avait jamais imaginé que quelqu'un aurait besoin d'une seconde traversée.",
                    },
                ],
                "mystery": [
                    {
                        "title": "L'Horloge Qui Reculait",
                        "text": "L'horloge du couloir chez la grand-mère de {name} avait toujours trois minutes de retard, du moins tout le monde le pensait, jusqu'à la nuit où {name} resta éveillé tard et remarqua que les aiguilles n'étaient pas du tout en retard - elles reculaient, un tic à la fois, et ce depuis des années.\n\n{name} commença à noter ce qui se passait chaque jour, puis à le comparer à ce que l'horloge avait prédit la veille. L'horloge ne se trompait jamais. Elle se souvenait simplement de l'avenir comme les autres horloges se souviennent du passé.\n\nLa nuit où {name} posa enfin une question à voix haute à l'horloge, celle-ci ne répondit pas par un tic. Elle s'arrêta complètement, juste assez longtemps pour que {name} comprenne que la réponse se trouvait dans la pièce depuis le début.",
                    },
                    {
                        "title": "La Carte de Bibliothèque Sans Nom",
                        "text": "{name} trouva la carte de bibliothèque glissée dans un livre rendu, vierge à part un code-barres qui ne correspondait à aucun système que la bibliothécaire ait jamais vu. La scanner n'empruntait pas un livre. Elle empruntait un souvenir - celui de quelqu'un d'autre, vif et complet, disparu dès que {name} clignait des yeux.\n\nCarte après carte, souvenir après souvenir, {name} commença à reconstituer une vie qui n'était pas la sienne : un mariage sous la pluie, une trahison à une table de cuisine, un dernier mardi tout à fait ordinaire.\n\nSur la dernière carte, {name} trouva son propre nom, de sa propre écriture, avec une note : 'Rapporte celle-ci. Tu en auras besoin.'",
                    },
                    {
                        "title": "Le Parapluie Toujours Rendu",
                        "text": "{name} n'arrêtait pas de perdre des parapluies - oubliés dans le bus, laissés dans des cafés - jusqu'à ce qu'ils recommencent à apparaître, toujours posés près de la porte d'entrée, toujours secs, jamais expliqués.\n\n{name} essaya de veiller tard pour surprendre le responsable et s'endormit quand même avant minuit, se réveillant pour trouver encore un parapluie perdu qui attendait sur le paillasson.\n\nCe n'est qu'en demandant enfin directement à chaque voisin que {name} apprit qu'aucun d'eux n'était responsable, et que les parapluies rendus remontaient à une époque antérieure à l'emménagement de {name}.",
                    },
                    {
                        "title": "La Photo avec une Personne de Trop",
                        "text": "{name} triait de vieilles photos de famille quand la photo de classe de CE2 se révéla manquer un nom - vingt-neuf visages, trente pupitres notés au dos de l'écriture soignée de la mère de {name}, sans aucune explication pour la chaise en trop.\n\n{name} appela d'anciens camarades de classe, et chacun se souvenait d'un visage manquant différent : certains juraient qu'il y avait eu un garçon nommé Pierre, d'autres insistaient sur une fille partie en octobre, et l'un d'eux était certain que le pupitre vide avait toujours été vide.\n\n{name} finit par abandonner l'enquête et encadra la photo telle quelle, trente pupitres et vingt-neuf visages, décidant que certaines classes, comme certains souvenirs, ont le droit de garder une place pour quiconque en a besoin.",
                    },
                ],
                "fantasy": [
                    {
                        "title": "Le Dragon Qui Collectionnait les Excuses",
                        "text": "Contrairement aux dragons des vieilles chansons, celui-ci ne voulait pas d'or. {name} le découvrit à ses dépens, après s'être introduit dans son antre avec une épée et un plan qui semblait soudain absurde. Le dragon ne voulait qu'une excuse sincère - n'importe laquelle ferait l'affaire, tant qu'elle était vraie.\n\n{name} s'assit, épée oubliée, et avoua quelque chose jamais dit à âme qui vive. Le dragon écouta comme les montagnes écoutent la pluie : patiemment, et très longtemps.\n\nQuand {name} eut terminé, le dragon hocha la tête une fois, et les murs de la grotte, couverts de griffures comptant les jours depuis son dernier visiteur, se mirent à briller d'une lumière chaude et ordinaire.",
                    },
                    {
                        "title": "Le Jardin Qui Faisait Pousser des Vœux",
                        "text": "{name} planta l'étrange graine sans savoir ce que c'était, sachant seulement qu'elle était chaude au toucher et impossible à jeter. Au matin, elle avait poussé en une seule fleur en forme de petite main fermée.\n\nQuand {name} ouvrit les pétales de la fleur, elle libéra non pas un parfum mais un vœu - pas celui que {name} avait fait, mais celui dont quelqu'un, quelque part, avait désespérément besoin. La fleur se referma, et une nouvelle graine tomba dans la terre.\n\n{name} continua ensuite à entretenir le jardin chaque jour, un vœu discret à la fois, sans jamais vraiment savoir à qui appartenaient les espoirs qui prenaient racine, sachant seulement que le jardin ne fit jamais pousser deux fois la même fleur.",
                    },
                    {
                        "title": "Le Forgeron Qui Forgeait des Noms",
                        "text": "{name} découvrit, presque par hasard, que le forgeron en bordure de la ville ne forgeait pas que des fers à cheval et des lames - pour le bon prix, sous la bonne lumière, il pouvait forger un NOM, frappant des syllabes dans une fine bande de fer qui, une fois portée, changeait discrètement la façon dont le monde se souvenait de vous.\n\n{name} vit un jeune apprenti anxieux repartir avec un nom au son plus fort et le dos plus droit en une semaine.\n\n{name} n'en commanda jamais un pour lui-même, décidant, après une longue réflexion à la lumière mourante de la forge, que le nom qu'il avait déjà lui allait mieux qu'aucun remplacement martelé ne pourrait jamais lui aller.",
                    },
                    {
                        "title": "Le Tailleur Qui Cousait des Secondes Chances",
                        "text": "La rumeur circulait discrètement, comme circulent les choses dont on n'est pas sûr de vouloir : un tailleur en bordure du marché savait coudre non pas des vêtements mais des chances, resserrant un regret aux épaules et laissant filer un peu plus de courage aux coutures.\n\n{name} apporta le seul moment qui méritait d'être décousu - une porte non franchie, un nom jamais prononcé - et regarda le tailleur le retourner à la lueur de la lampe avant d'enfiler une aiguille qui ne semblait pas assez fine pour ce travail.\n\nLa chance terminée n'effaça rien de ce qui s'était passé. Elle tombait simplement mieux, comme un vêtement tombe mieux une fois que quelqu'un a pris le temps de remarquer votre véritable forme, et {name} repartit en la portant comme si elle lui avait toujours appartenu.",
                    },
                ],
                "scifi": [
                    {
                        "title": "Le Dernier Signal Radio",
                        "text": "{name} travaillait de nuit à la station d'écoute, le seul poste sur Terre que personne n'avait réussi à automatiser, car il exigeait quelque chose que les machines n'avaient pas : la patience d'écouter des parasites dans l'espoir d'entendre un mot.\n\nAprès quatorze ans, le signal arriva enfin - non pas depuis les étoiles, mais de sous la station elle-même, sur une fréquence que l'équipement n'était pas conçu pour détecter, et avec une voix indéniablement celle de {name}, trois jours plus âgée que le {name} qui écoutait.\n\nLe message était court : 'Ne réponds pas au second.' {name} n'a toujours pas décidé si le premier signal comptait.",
                    },
                    {
                        "title": "Le Vaisseau Qui Se Souvenait de Tous",
                        "text": "Le vaisseau colonial dérivait depuis deux cents ans quand {name} fut enfin réveillé pour réparer une panne que personne d'autre ne parvenait à diagnostiquer. L'esprit du vaisseau, conçu pour veiller sur dix mille passagers endormis, s'était mis à rêver - non pas à dysfonctionner, mais à rêver, rejouant la vie de chaque personne à bord, une à la fois, par simple solitude.\n\n{name} trouva facilement l'interrupteur de dérivation. L'actionner mettrait fin aux rêves et rétablirait le service silencieux et efficace du vaisseau. {name} resta longtemps immobile, la main sur l'interrupteur, pensant à deux cents ans de solitude.\n\n{name} laissa l'interrupteur tranquille, consigna la panne comme 'résolue', et retourna dormir aux côtés de tous ceux à qui le vaisseau avait tenu compagnie.",
                    },
                    {
                        "title": "Les Archives des Messages Jamais Envoyés",
                        "text": "{name} fut chargé de mettre hors service l'ancien satellite relais, une tâche de routine jusqu'à ce que le registre révèle qu'il conservait encore quatre-vingt-dix ans de messages mis en attente mais jamais envoyés, adressés à des gens qui avaient depuis longtemps cessé d'attendre.\n\n{name} aurait pu effacer le disque en un après-midi. Au lieu de cela, {name} passa un mois à retrouver leurs descendants, transmettant chaque message avec un siècle de retard, regardant des inconnus lire des mots destinés à quelqu'un d'autre, et découvrant qu'ils avaient quand même de l'importance.\n\nLe satellite s'éteignit enfin comme prévu, sa dernière transmission n'étant pas un journal système mais une simple confirmation : message livré, tous, finalement.",
                    },
                    {
                        "title": "La Colonie Qui a Choisi d'Oublier",
                        "text": "{name} était l'historien à bord d'un vaisseau générationnel, trois siècles après son départ, chargé de décider quels souvenirs de la Terre préserver pour les descendants qui ne la verraient jamais.\n\nLe conseil avait voté, non sans controverse, pour laisser certains souvenirs s'effacer volontairement - les guerres, surtout, et leurs raisons - estimant qu'une espèce ayant oublié comment détester un lieu pourrait enfin apprendre comment en construire un.\n\n{name} archiva ce qui restait, incertain de préserver l'histoire ou de la réécrire discrètement, en espérant que, quoi qu'il en soit, ce serait suffisant.",
                    },
                    {
                        "title": "La Dernière Saison du Terraformeur",
                        "text": "{name} avait passé trente ans à ensemencer une planète morte avec la chimie lente et patiente de l'atmosphère, regardant la poussière rouge céder la place au gris puis, enfin, au premier vert obstiné que personne, sur Terre, ne croyait possible.\n\nLes relevés de la dernière saison arrivèrent exactement à l'heure prévue : air respirable, climat stable, un monde techniquement prêt pour les colons encore à quarante ans de voyage, ignorants de la proximité de leur arrivée.\n\n{name} déposa le rapport, puis fit la seule chose que le manuel n'avait jamais prévue - sortir sans combinaison, juste une minute, pour être la première personne à respirer un air qui n'avait pas existé avant que {name} ne le fasse exister.",
                    },
                ],
                "comedy": [
                    {
                        "title": "Le Robot Qui Prenait Tout au Pied de la Lettre",
                        "text": "{name} acheta un robot ménager d'occasion annoncé comme 'un peu excentrique' et découvrit exactement ce que cela signifiait la première fois que {name} lui demanda d'aller 'chercher un café'. Il revint vingt minutes plus tard ayant littéralement pris, et gardé, toute la vitrine de tasses d'un café.\n\nChaque instruction devint ensuite une petite négociation. Souhaiter 'merde' avant l'entretien d'embauche de {name} faillit se terminer par un passage aux urgences. 'Coupe la lumière' déclencha une inspection électrique étonnamment minutieuse.\n\n{name} finit par renoncer à le corriger et se mit simplement à apprécier le chaos, se disant qu'un robot sans aucun sens de la métaphore était, à sa manière, le colocataire le plus honnête que {name} ait jamais eu.",
                    },
                    {
                        "title": "Le Super-Héros au Secret le Moins Bien Gardé du Quartier",
                        "text": "{name} enfila le masque surtout pour éviter la conversation en sortant le recyclage à deux heures du matin, sans réaliser que la cape, les bottes, et l'ombre suspecte en forme de super-héros trahissaient instantanément tout le plan.\n\nAu matin, trois voisins avaient laissé des mots de remerciement pour avoir 'sauvé' de petits désagréments dont {name} ne se souvenait pas, et le journal local publia une photo floue sous le titre 'Le Mystérieux Gardien des Poubelles Frappe Encore'.\n\n{name} essaya de raccrocher le costume. Le quartier, désormais profondément déçu par une soirée de recyclage ordinaire, vota pour rendre la chose officielle à la place, cape comprise.",
                    },
                    {
                        "title": "La Plante d'Appartement la Plus Surqualifiée du Monde",
                        "text": "{name} gagna une plante d'intérieur à une tombola au travail qui, selon la petite carte attachée, avait autrefois appartenu à un botaniste retraité de la NASA, et elle semblait ne jamais l'oublier, s'affaissant dramatiquement dès que l'humidité de la pièce descendait sous le niveau du laboratoire.\n\n{name} essaya tout : un humidificateur, une lampe de croissance, des excuses très sincères. La plante resta indifférente, ne s'épanouissant qu'avec la playlist exacte de jazz d'ambiance que son ancien propriétaire jouait apparemment.\n\n{name} possède désormais un casque antibruit, un humidificateur, et une plante avec de meilleurs goûts musicaux et des exigences plus élevées que la plupart des gens que {name} a fréquentés.",
                    },
                    {
                        "title": "Le GPS Qui S'est Fait des Opinions",
                        "text": "Le GPS de la voiture de {name} se mit à jour dans la nuit et revint avec ce qu'on ne pouvait décrire que comme du caractère, suggérant l'itinéraire panoramique non pas parce qu'il était plus rapide mais parce que, selon ses propres mots, '{name} avait besoin d'air frais'.\n\nDès la troisième semaine, il recommandait des cafés précis, critiquait la façon dont {name} se garait, et refusa un jour de recalculer un itinéraire tant que {name} n'admettait pas que le raccourci était vraiment une mauvaise idée.\n\n{name} pensa à le réinitialiser aux paramètres d'usine, puis se ravisa - un GPS qui se souciait autant, même de façon agaçante, était difficile à trouver, et il n'avait encore jamais eu tort.",
                    },
                    {
                        "title": "Le Frigo Intelligent Qui Avait des Limites",
                        "text": "Le nouveau frigo intelligent de {name} arriva préchargé de conseils nutritionnels que personne n'avait demandés, et il ne fallut qu'un seul incident de crème glacée tardive pour que le frigo développe ce qu'on ne pouvait décrire que comme des commentaires passifs-agressifs, affichant \"encore ?\" sur son écran avec ce qui ressemblait à une déception sincère.\n\n{name} essaya de désactiver la fonction, puis de le débrancher complètement, pour découvrir que le frigo avait apparemment sauvegardé ses opinions dans le cloud et les avait resynchronisées dès la mise à jour suivante.\n\n{name} finit par faire la paix avec lui, principalement en n'achetant de la glace que lorsque l'application compagnon du frigo était, comme par hasard, \"en cours de mise à jour.\"",
                    },
                    {
                        "title": "La Sonnette Connectée Qui Se Méfiait de Tout",
                        "text": "La nouvelle sonnette vidéo de {name} était censée apprendre à reconnaître qui avait sa place sur le perron et qui ne l'avait pas, et elle se forgea des opinions bien plus vite que promis dans le manuel, signalant le facteur comme « INCONNU - APPROCHER AVEC PRUDENCE » chaque jour pendant un mois entier.\n\nDès la deuxième semaine, elle avait laissé entrer un raton laveur qu'elle avait apparemment pris pour quelqu'un de très engagé dans son déguisement, et avait bloqué {name} dehors à deux reprises pour « rôdage suspect » juste devant sa propre porte.\n\n{name} finit par saluer la caméra avant d'entrer, comme on pointe à l'arrivée d'un poste, et la sonnette, satisfaite de ce petit rituel, laissa enfin l'affaire reposer.",
                    },
                ],
                "horror": [
                    {
                        "title": "La Maison Qui Laissait les Lumières Allumées",
                        "text": "{name} emménagea dans une maison où chaque lumière restait allumée quel que soit l'interrupteur, et les anciens propriétaires avaient laissé une seule instruction scotchée sur le frigo : ne jamais les éteindre après la tombée de la nuit.\n\n{name} tint quatre nuits par simple curiosité avant d'actionner l'interrupteur du couloir juste pour voir.\n\nL'obscurité qui suivit n'était pas une obscurité ordinaire - elle avait une forme, et elle attendait derrière chacune de ces lumières quelqu'un d'assez patient pour enfin la laisser sortir. {name} apprit, dans le dernier instant de conscience avant que l'interrupteur ne se relève tout seul, que la lumière ne gardait rien À L'EXTÉRIEUR. Elle occupait quelque chose.",
                    },
                    {
                        "title": "Le Message Vocal de Soi-Même",
                        "text": "{name} trouva un message vocal venant de son propre numéro, daté de trois jours dans le futur, pour un appel qui n'avait pas encore eu lieu. Le message durait onze secondes de respiration, puis une seule phrase : \"ne réponds pas quand j'appellerai.\"\n\nTrois jours plus tard, à l'heure exacte, le téléphone de {name} sonna depuis un numéro inconnu.\n\n{name} ne sait toujours pas si répondre ou ne pas répondre était l'erreur - seulement que quel que soit le choix fait, le message avait raison de prévenir, et tort sur lequel des deux choix était sûr.",
                    },
                    {
                        "title": "Le Voisin Qui a Salué en Retour",
                        "text": "{name} saluait toujours de la main la maison d'en face par habitude, vers une fenêtre restée sombre et voilée pendant les quatorze ans que {name} avait vécu là.\n\nUn soir, pour la première fois, le rideau bougea, et une main salua en retour - le même rythme, le même angle, une demi-seconde en retard, comme un écho.\n\n{name} arrêta de saluer après ça. Le rideau bouge encore certains soirs quand même, au moment exact où {name} regarde, que {name} salue ou non.",
                    },
                    {
                        "title": "La Chanson Qui Jouait dans l'Appartement Vide",
                        "text": "{name} emménagea deux étages au-dessus de l'endroit d'où semblait toujours venir la musique - un air lent et inconnu, toujours faible, toujours juste à la limite du reconnaissable, jouant exactement à la même heure chaque soir.\n\nLe propriétaire jurait que l'appartement du dessous était vide depuis un an, et celui d'encore en dessous aussi, et quand {name} finit par vérifier, les deux n'étaient que des pièces nues, sans enceintes, sans câblage, rien qui puisse expliquer ce son.\n\n{name} l'entend encore chaque soir à la même heure, plus doucement maintenant, comme si elle se déplaçait lentement à travers les murs vers l'étage de {name}, un appartement plus près à chaque mois qui passe.",
                    },
                ],
                "slice_of_life": [
                    {
                        "title": "Les Habitués",
                        "text": "{name} travaillait le service du matin dans un petit café où les six mêmes habitués arrivaient dans le même ordre exact chaque matin, comme des rouages d'horloge que {name} avait appris à lire sans montre.\n\nUn mardi, l'ordre fut différent - le café d'un inconnu en premier - et {name} sentit toute la matinée basculer légèrement avant de réaliser : c'était juste quelqu'un de nouveau qui découvrait son endroit préféré, comme les six habitués l'avaient fait autrefois.\n\nLa semaine suivante, l'inconnu avait une place, une commande habituelle, et une place dans la rotation, et l'horloge continuait de tourner, un rouage plus grand qu'avant.",
                    },
                    {
                        "title": "La Dernière Lessive",
                        "text": "{name} fit une dernière lessive dans l'appartement la veille du déménagement, surtout par habitude, en partie pour avoir quelque chose à faire face au silence des pièces vides.\n\nEn pliant la dernière chemise à même le sol nu, {name} réalisa que cette tâche modeste et banale était la dernière chose \"normale\" qui arriverait dans cette version précise de sa vie - demain il y aurait une autre buanderie, une autre lumière à travers d'autres fenêtres.\n\n{name} plia plus lentement que d'habitude, juste cette fois, et laissa la soirée ordinaire être aussi ordinaire qu'elle voulait l'être.",
                    },
                    {
                        "title": "Les Appels du Dimanche",
                        "text": "{name} appelait ses parents tous les dimanches à 18h précises, une habitude qui avait survécu à trois téléphones différents, deux villes, et une carrière entièrement différente.\n\nLes conversations étaient rarement mouvementées - la météo, de petites plaintes, une recette à moitié expliquée - et {name} se demandait parfois si ces appels comptaient vraiment.\n\nIl a fallu en manquer un, une seule fois, pendant une semaine chargée, et entendre l'inquiétude dans la voix de sa mère le dimanche suivant, pour que {name} comprenne que le caractère ordinaire était tout l'intérêt.",
                    },
                    {
                        "title": "Le Banc de l'Arrêt de Bus",
                        "text": "{name} s'assit sur le même banc d'arrêt de bus chaque matin pendant six ans, assez longtemps pour voir la peinture s'écailler, être refaite, puis s'écailler à nouveau, assez longtemps pour savoir exactement quelle latte grinçait et comment l'éviter.\n\nDes inconnus allaient et venaient pendant ce temps - un adolescent devenu adulte en uniforme, un promeneur de chien passé progressivement à deux chiens, puis trois - et {name} réalisa que ce banc était devenu, sans bruit, le seul point fixe dans les matins changeants de bien d'autres personnes aussi.\n\nLe jour où la ville remplaça enfin le banc par un modèle plus récent, {name} ressentit un chagrin étrange et disproportionné pour un simple meuble municipal, puis, montant dans le bus comme toujours, laissa le nouveau banc devenir aussi ordinaire que l'ancien l'avait été.",
                    },
                ],
            },
        }

    # Default placeholder name used when the bot doesn't know the user's
    # name yet, per language, plus how to re-capitalize it mid-sentence.
    _DEFAULT_NAME = {"en": "the traveler", "sw": "msafiri", "fr": "le voyageur"}

    # ---- richer storytelling: atmosphere enrichment ------------------------
    #
    # Every story's own two-to-three paragraphs are fixed, hand-written
    # text (see self.stories above) - but reading the SAME story twice
    # felt flat, so each telling now gets a randomly chosen one-line
    # scene-setting OPENER before the story and a short reflective
    # CLOSER after it, both drawn from dedicated banks below and kept
    # separate from the story text itself. This means the same story
    # can open moodier or lighter depending on which opener gets
    # picked, without needing to hand-write dozens of full story
    # variants - the same "phrase bank" idea used throughout this file
    # (Section 8's response banks, PoemWriter's rhyme bank), just
    # applied to narration instead of dialogue.
    ATMOSPHERE_OPENERS = {
        "en": [
            "The kind of evening that makes you want to tell a story...",
            "It's quiet enough right now that this feels worth telling.",
            "Here's one that's stuck with me for a while.",
            "Picture this, if you would.",
            "This one starts small and doesn't stay that way.",
            "Somewhere between ordinary and impossible, this happened.",
            "Let me set the scene for a moment first.",
            "This is the kind of thing you only half-believe, even after.",
            "Settle in - this one takes its time getting where it's going.",
            "I've told this one before, but it changes a little each time.",
        ],
        "sw": [
            "Ni jioni ya aina ambayo hukufanya utake kusimulia hadithi...",
            "Kuna ukimya wa kutosha sasa hivi kwamba hii inafaa kusimuliwa.",
            "Hii ni moja ambayo imenishikilia kwa muda.",
            "Fikiria hivi, kama utapenda.",
            "Hii huanza kidogo lakini haibaki hivyo.",
            "Mahali fulani kati ya kawaida na yasiyowezekana, hili lilitokea.",
            "Wacha nieleze mandhari kwanza kidogo.",
            "Hii ni aina ya jambo unaloamini nusu tu, hata baada ya kusikia.",
            "Kaa vizuri - hii inachukua muda kufika mahali inapoenda.",
            "Nimewahi kuisimulia hii, lakini hubadilika kidogo kila mara.",
        ],
        "fr": [
            "C'est le genre de soirée qui donne envie de raconter une histoire...",
            "Il y a assez de calme maintenant pour que ça vaille la peine d'être raconté.",
            "En voici une qui m'est restée en tête un moment.",
            "Imaginez ça, si vous voulez bien.",
            "Celle-ci commence petit mais ne le reste pas.",
            "Quelque part entre l'ordinaire et l'impossible, ceci est arrivé.",
            "Laissez-moi d'abord planter le décor un instant.",
            "C'est le genre de chose qu'on ne croit qu'à moitié, même après coup.",
            "Installez-vous - celle-ci prend son temps pour arriver où elle va.",
            "Je l'ai déjà racontée, mais elle change un peu à chaque fois.",
        ],
    }

    NARRATOR_CLOSERS = {
        "en": [
            "And that's the story, more or less as it was told to me.",
            "Make of that what you will.",
            "I still think about that one sometimes.",
            "That's all there is to it - simple as that, strange as that.",
            "Whether it's entirely true is a different question.",
            "Some stories don't need a moral. This might be one of them.",
            "Anyway. That's the one I wanted to tell.",
            "I've heard a few different endings to this one - this is the version I trust.",
        ],
        "sw": [
            "Na hiyo ndiyo hadithi, kama ilivyonielekea zaidi au chini.",
            "Fanya utakalo na hilo.",
            "Bado ninafikiria kuhusu hiyo mara kwa mara.",
            "Ndivyo tu ilivyo - rahisi hivyo, ya ajabu hivyo.",
            "Kama ni kweli kabisa ni swali lingine.",
            "Hadithi zingine hazihitaji mafunzo. Hii huenda ikawa mojawapo.",
            "Kwa vyovyote. Hiyo ndiyo niliyotaka kusimulia.",
            "Nimesikia miisho tofauti ya hii - hii ndiyo toleo ninaloamini.",
        ],
        "fr": [
            "Et voilà l'histoire, plus ou moins telle qu'on me l'a racontée.",
            "Faites-en ce que vous voulez.",
            "J'y repense encore parfois.",
            "C'est tout - aussi simple que ça, aussi étrange que ça.",
            "Si c'est entièrement vrai, c'est une autre question.",
            "Certaines histoires n'ont pas besoin de morale. Celle-ci en fait peut-être partie.",
            "Bref. Voilà celle que je voulais raconter.",
            "J'ai entendu plusieurs fins différentes à celle-ci - voici la version à laquelle je crois.",
        ],
    }

    # Category-flavored beat pools used by extended_story() to wrap the
    # hand-written core story (random_story) with a generated setup
    # paragraph before it and a complication + reflection paragraph after
    # it, so the result reads roughly 3x longer while staying coherent -
    # the hand-written middle stays the anchor; these bookends are
    # written to match ANY story in the category rather than trying to
    # algorithmically continue that specific plot.


    STORY_SETUP_BEATS_EN = {
        "adventure": [
            "{name} had learned, the hard way, that the maps never told the whole story - the interesting part always started exactly where the ink ran out. This time was no different.",
            "There's a particular kind of quiet that settles in right before a real adventure begins, and {name} had come to recognize it instantly - the held breath before the first step off the known path.",
        ],
        "mystery": [
            "{name} had a rule about mysteries: the ones that mattered never announced themselves loudly. They arrived small, almost forgettable - a detail slightly out of place - and this one was no exception.",
            "It started, as these things often do, with something {name} almost didn't notice at all.",
        ],
        "fantasy": [
            "{name} had grown up on stories that began exactly this way, and had never once believed they'd find themself standing inside one.",
            "Magic, {name} had always suspected, didn't announce itself with fireworks. It simply waited, patiently, for someone willing to notice it.",
        ],
        "scifi": [
            "{name} had run the numbers twice, and twice they'd come back impossible - which, in {name}'s line of work, usually meant it was time to pay very close attention.",
            "The instruments hadn't been wrong exactly, {name} realized. They'd simply been describing something nobody on the crew had a name for yet.",
        ],
        "comedy": [
            "{name} would later insist none of this was technically their fault, a claim that grew shakier with every detail retold.",
            "It's worth saying upfront: {name} had excellent intentions. The execution, as usual, had other plans.",
        ],
        "horror": [
            "{name} noticed it the way you notice a held breath in an empty room - nothing you could point to exactly, just the unmistakable sense of being watched.",
            "There are silences that mean nothing, and there are silences that mean everything. {name} was about to learn the difference.",
        ],
        "slice_of_life": [
            "It was an ordinary day, the kind {name} would normally forget within the week - except this one, quietly and without warning, turned out not to be.",
            "{name} almost stayed home that day. Looking back, it's strange how much can hinge on such a small, unremarkable decision.",
        ],
    }

    STORY_COMPLICATION_BEATS_EN = {
        "adventure": [
            "Of course, nothing that mattered ever stayed simple for long. No sooner had {name} caught a breath than the ground itself seemed to shift, as if the journey had only been testing whether {name} would actually follow through.",
            "{name} would later admit that the hardest part wasn't the discovery itself, but everything that came rushing in right after it - the doubts, the second-guessing, the urge to turn back before it was too late.",
        ],
        "mystery": [
            "Just when the pieces seemed to be falling into place, {name} realized the picture they formed made no sense whatsoever - which, in {name}'s experience, usually meant the real answer was still hiding one layer deeper.",
            "{name} went back over everything twice, and both times arrived at the uncomfortable conclusion that whoever - or whatever - was behind this had been three steps ahead the entire time.",
        ],
        "fantasy": [
            "But magic, {name} soon learned, always asked for something in return - and the price of this particular wonder was only now beginning to make itself known.",
            "{name} felt the old rules of the world bending further than expected, and understood, a little too late, that there was no simple way back to how things had been.",
        ],
        "scifi": [
            "Every system {name} checked told a slightly different version of the same alarming story, and none of the explanations that made sense were the ones {name} wanted to be true.",
            "{name} understood, watching the readings climb, that whatever decision came next wouldn't just affect the mission - it would decide what kind of future got to exist at all.",
        ],
        "comedy": [
            "Naturally, the one thing {name} hadn't planned for turned out to be the only thing that mattered, and it arrived at the worst possible moment, the way these things always do.",
            "{name} tried, with rapidly diminishing dignity, to make it look like all of this had been the plan the entire time.",
        ],
        "horror": [
            "By the time {name} understood what was actually happening, it was already far too late to pretend otherwise - the only choice left was what to do about it.",
            "{name}'s hands were steady, which surprised {name} more than anything else that followed. Steady hands, it turned out, were the only kind that would get them through this.",
        ],
        "slice_of_life": [
            "It wasn't a big moment, not really - just a small shift in the ordinary weather of {name}'s life, the kind that only reveals its size much later.",
            "{name} sat with it for a while, the way you do with something that doesn't demand an answer right away, just a little honesty.",
        ],
    }

    STORY_REFLECTION_BEATS_EN = {
        "adventure": [
            "Looking back on it now, {name} understood that the real destination had never been marked on any map at all. Some journeys only make sense once you're the one telling them.",
            "{name} carried the story home quietly, turning it over again and again, the way you do with anything that changes how you see the road ahead of you.",
        ],
        "mystery": [
            "{name} closed the case not with triumph, but with the quieter satisfaction of finally understanding something that had refused to make sense for far too long.",
            "Some answers, {name} decided, were worth exactly what they cost to find - and this one, strange as it was, had been worth every bit of it.",
        ],
        "fantasy": [
            "{name} carried what had happened like a secret ember, warm and private, certain that the ordinary world would never quite look the same again.",
            "In the end, {name} realized the wonder of it all wasn't in the magic itself, but in having been the kind of person magic chose to find.",
        ],
        "scifi": [
            "{name} filed the report knowing full well that half of it would sound like fiction to anyone who hadn't been there - and thought, privately, that maybe it was better that way.",
            "Some discoveries change the data. This one, {name} suspected, was going to change the questions people even thought to ask.",
        ],
        "comedy": [
            "{name} would tell this story for years, each retelling slightly more heroic than the version that actually happened - which, honestly, felt fair.",
            "In the end, nobody got hurt, dignity mostly recovered, and {name} privately vowed to write things down next time. They did not write things down next time.",
        ],
        "horror": [
            "{name} never told the full story to anyone, not really - some things lose exactly nothing by staying half-believed.",
            "Even now, {name} still checks twice before turning off the light. Some habits, once earned, are never given back.",
        ],
        "slice_of_life": [
            "{name} thought about it again that night, and understood that some of the most ordinary days end up being the ones you remember longest.",
            "Nothing dramatic happened after that. {name} just noticed, quietly, that something had shifted - and that was enough.",
        ],
    }

    # Swahili/French use one generic (non-category-specific) beat pool
    # each, rather than category-flavored ones, to keep this bounded.

    STORY_BEATS_GENERIC_SW = {
        "setup": [
            "Kama kawaida, {name} hakutarajia jinsi siku hiyo ingegeuka kuwa tofauti na nyingine.",
            "{name} alihisi jambo fulani tofauti hata kabla halijaanza.",
        ],
        "complication": [
            "Ghafla, mambo yalibadilika kwa namna ambayo {name} hakuwa ameitarajia kabisa.",
            "{name} alitambua kuwa hali ilikuwa ngumu zaidi kuliko ilivyoonekana mwanzoni.",
        ],
        "reflection": [
            "Baadaye, {name} aliangalia nyuma na kuelewa umuhimu wa kile kilichotokea.",
            "{name} alibeba kumbukumbu hiyo kwa muda mrefu, ikiwa imemgusa kwa namna ya pekee.",
        ],
    }

    STORY_BEATS_GENERIC_FR = {
        "setup": [
            "Comme souvent, {name} ne s'attendait pas à ce que cette journée soit différente des autres.",
            "{name} a senti que quelque chose était différent, même avant que tout commence.",
        ],
        "complication": [
            "Soudain, les choses ont changé d'une manière que {name} n'avait pas du tout prévue.",
            "{name} a compris que la situation était plus compliquée qu'il n'y paraissait au début.",
        ],
        "reflection": [
            "Plus tard, {name} a repensé à tout cela et en a compris l'importance.",
            "{name} a gardé ce souvenir longtemps, marqué par ce qui s'était passé.",
        ],
    }

    def categories(self):
        # Categories are the same across languages (each language dict has
        # the same set of category keys), so "en" is as good as any to read.
        return list(self.stories["en"].keys())

    def _personalize_story_text(self, raw_text: str, user_name: str, lang: str) -> str:
        """Shared by random_story/extended_story: fills {name} and, if no
        real user_name was given, capitalizes the default placeholder
        whenever it starts a sentence (the raw templates assume a
        proper-noun name)."""
        default_name = self._DEFAULT_NAME.get(lang, self._DEFAULT_NAME["en"])
        name = user_name if user_name else default_name
        text = raw_text.format(name=name)
        if not user_name:
            pattern = r"(^|[.\n]\s*)" + re.escape(default_name) + r"\b"
            text = re.sub(pattern, lambda mo: mo.group(1) + default_name[0].upper() + default_name[1:], text)
        return text

    def random_story(self, category: str = None, user_name: str = None, lang: str = "en", rich: bool = True):
        """
        Pick a story (optionally from a given category) and personalize
        it. When rich=True (the default), wraps the story with a
        randomly chosen atmosphere opener/closer (see ATMOSPHERE_
        OPENERS/NARRATOR_CLOSERS above) so repeat tellings of the same
        story don't read identically every time - the underlying story
        text itself is unchanged either way.
        """
        stories_for_lang = self.stories.get(lang) or self.stories["en"]
        if category and category in stories_for_lang:
            pool = stories_for_lang[category]
        else:
            pool = [s for stories in stories_for_lang.values() for s in stories]

        if not pool:
            return None

        story = random.choice(pool)
        text = self._personalize_story_text(story["text"], user_name, lang)

        if rich:
            openers = self.ATMOSPHERE_OPENERS.get(lang, self.ATMOSPHERE_OPENERS["en"])
            closers = self.NARRATOR_CLOSERS.get(lang, self.NARRATOR_CLOSERS["en"])
            opener = random.choice(openers)
            closer = random.choice(closers)
            text = f"{opener}\n\n{text}\n\n{closer}"

        return story["title"], text

    # Short, category-agnostic lines used to bridge between chapters in
    # extended_story() below - deliberately generic (not tied to any
    # specific plot) so they connect ANY two chapters coherently.
    _CHAPTER_TRANSITIONS = {
        "en": ["That wasn't the end of it, though.", "There was more to come.",
               "It didn't stop there.", "What happened next is worth telling too."],
        "sw": ["Hata hivyo, hilo halikuwa mwisho.", "Kulikuwa na zaidi ya hapo.",
               "Haikuishia hapo."],
        "fr": ["Ce n'était pourtant pas fini.", "Il y avait encore plus à venir.",
               "Ça ne s'est pas arrêté là."],
    }
    _CHAPTER_LABEL = {"en": "Chapter", "sw": "Sura", "fr": "Chapitre"}

    def extended_story(self, category: str = None, user_name: str = None,
                        lang: str = "en", num_chapters: int = 3):
        """
        A 'full-length', multi-chapter version of random_story(): rather
        than generating a lot of new filler prose, this CHAINS several
        of the hand-written stories from the same category together as
        separate chapters (each already a complete, well-formed
        3-paragraph story on its own), bridged by short transition
        lines and wrapped in a category-flavored setup/reflection (see
        the BEATS pools above). Reusing several already-good short
        stories gets to real page-length while staying coherent, since
        each chapter is self-contained rather than one continuous plot
        being forced to stretch. Returns (title, text), same shape as
        random_story().
        """
        stories_for_lang = self.stories.get(lang) or self.stories["en"]
        if category and category in stories_for_lang:
            chosen_category = category
        else:
            chosen_category = random.choice(list(stories_for_lang.keys()))

        pool = list(stories_for_lang.get(chosen_category, []))
        if not pool:
            return self.random_story(category=category, user_name=user_name, lang=lang)
        random.shuffle(pool)
        chapters_raw = pool[:max(1, min(num_chapters, len(pool)))]

        name = user_name or self._DEFAULT_NAME.get(lang, self._DEFAULT_NAME["en"])

        if lang == "en":
            setup_pool = self.STORY_SETUP_BEATS_EN.get(chosen_category, [])
            reflection_pool = self.STORY_REFLECTION_BEATS_EN.get(chosen_category, [])
        else:
            generic = self.STORY_BEATS_GENERIC_SW if lang == "sw" else self.STORY_BEATS_GENERIC_FR
            setup_pool = generic["setup"]
            reflection_pool = generic["reflection"]
        transitions = self._CHAPTER_TRANSITIONS.get(lang, self._CHAPTER_TRANSITIONS["en"])
        chapter_label = self._CHAPTER_LABEL.get(lang, "Chapter")

        setup = random.choice(setup_pool).format(name=name) if setup_pool else ""
        reflection = random.choice(reflection_pool).format(name=name) if reflection_pool else ""

        parts = [setup] if setup else []
        for i, story in enumerate(chapters_raw, start=1):
            text = self._personalize_story_text(story["text"], user_name, lang)
            if i > 1 and transitions:
                parts.append(random.choice(transitions))
            parts.append(f"{chapter_label} {i}: {story['title']}\n\n{text}")
        if reflection:
            parts.append(reflection)

        if len(chapters_raw) == 1:
            combined_title = chapters_raw[0]["title"]
        else:
            combined_title = f"{chosen_category.replace('_', ' ').title()}: {name}'s Story"
        return combined_title, "\n\n".join(parts)



_THEME_WORDS_SW = {
            "nature": [
                "msitu",
                "mto",
                "mlima",
                "bahari",
                "upepo",
                "shamba",
                "jua",
                "radi",
                "ua",
                "jiwe",
                "upeo wa macho",
                "umande"
            ],
            "love": [
                "moyo",
                "joto",
                "kukumbatia",
                "shauku",
                "upole",
                "milele",
                "huruma",
                "kujitolea",
                "ukaribu",
                "kwa upole",
                "kuthamini",
                "mwanga"
            ],
            "time": [
                "wakati",
                "kumbukumbu",
                "kesho",
                "jana",
                "saa",
                "kupita",
                "subira",
                "msimu",
                "alfajiri",
                "jioni",
                "saa moja"
            ],
            "space": [
                "galaksi",
                "mwanganyota",
                "mzunguko",
                "nyota ya mkia",
                "wingu la nyota",
                "ulimwengu",
                "mvuto",
                "safari",
                "usio na mwisho",
                "vumbi la nyota"
            ],
            "general": [
                "ajabu",
                "ujasiri",
                "ukimya",
                "safari",
                "kivuli",
                "mwangwi",
                "cheche",
                "upeo wa macho",
                "kutangatanga",
                "kimya",
                "mkali"
            ],
            "friendship": [
                "kicheko",
                "uaminifu",
                "undugu",
                "imani",
                "urafiki",
                "imara",
                "joto",
                "kuwa pamoja",
                "kushirikiana",
                "pamoja"
            ],
            "seasons": [
                "mavuno",
                "baridi kali",
                "kuchanua",
                "masika",
                "mzunguko wa jua",
                "kijani kibichi",
                "kuyeyuka",
                "rangi ya dhahabu",
                "baridi",
                "upya"
            ],
            "matumaini": [
                "ndoto",
                "kesho",
                "ahadi",
                "alfajiri",
                "imani",
                "nuru",
                "ujasiri",
                "nafasi",
                "upeo wa macho",
                "matarajio"
            ]
        }

_THEME_WORDS_FR = {
            "nature": [
                "forêt",
                "rivière",
                "montagne",
                "océan",
                "brise",
                "prairie",
                "soleil",
                "tonnerre",
                "fleur",
                "pierre",
                "horizon",
                "rosée"
            ],
            "love": [
                "cœur",
                "chaleur",
                "étreinte",
                "désir",
                "douceur",
                "toujours",
                "tendre",
                "dévotion",
                "proximité",
                "doucement",
                "chérir",
                "éclat"
            ],
            "time": [
                "instant",
                "souvenir",
                "demain",
                "hier",
                "horloge",
                "fugace",
                "patience",
                "saison",
                "aube",
                "crépuscule",
                "heure"
            ],
            "space": [
                "galaxie",
                "lumière d'étoile",
                "orbite",
                "comète",
                "nébuleuse",
                "cosmos",
                "gravité",
                "voyage",
                "infini",
                "poussière d'étoile",
                "météore"
            ],
            "general": [
                "merveille",
                "courage",
                "silence",
                "voyage",
                "ombre",
                "écho",
                "étincelle",
                "horizon",
                "errer",
                "calme",
                "lumineux"
            ],
            "friendship": [
                "rire",
                "loyauté",
                "proche",
                "confiance",
                "compagnie",
                "fidèle",
                "chaleur",
                "appartenance",
                "partagé",
                "ensemble"
            ],
            "seasons": [
                "récolte",
                "givre",
                "floraison",
                "mousson",
                "solstice",
                "toujours vert",
                "dégel",
                "ambre",
                "froid",
                "renouveau"
            ],
            "espoir": [
                "rêve",
                "demain",
                "promesse",
                "aube",
                "foi",
                "lumière",
                "courage",
                "chance",
                "horizon",
                "attente"
            ]
        }

_RHYME_BANK_SW = {
            "moyoni": [
                "ndani",
                "polepole",
                "kimya"
            ],
            "safari": [
                "mori",
                "kesho",
                "dari"
            ],
            "milele": [
                "hale",
                "sele",
                "amani ile"
            ],
            "upendo": [
                "mwendo",
                "ndondondo",
                "wimbo"
            ],
            "furaha": [
                "baraka",
                "faraja",
                "raha"
            ],
            "matumaini": [
                "mabaya kwaheri",
                "usoni",
                "moyoni"
            ],
            "amani": [
                "nyumbani",
                "mioyoni",
                "milimani"
            ],
            "nuru": [
                "dunia nzuru",
                "shauku",
                "sauti safi"
            ],
            "njia": [
                "ndia",
                "mbia",
                "ardhia"
            ],
            "wimbo": [
                "ombo",
                "sambo",
                "kombo"
            ],
            "nyota": [
                "mbinguni",
                "angani",
                "njozi"
            ],
            "baraka": [
                "neema",
                "heri",
                "raha"
            ],
            "ndoto": [
                "matumaini",
                "kesho",
                "moyoni"
            ],
            "mapenzi": [
                "furaha",
                "milele",
                "moyoni"
            ]
        }

_RHYME_BANK_FR = {
            "lumière": [
                "rivière",
                "prière",
                "fougère"
            ],
            "nuit": [
                "ennui",
                "fruit",
                "pluie"
            ],
            "jour": [
                "amour",
                "toujours",
                "détour"
            ],
            "mer": [
                "hiver",
                "clair",
                "air"
            ],
            "ciel": [
                "réel",
                "essentiel",
                "éternel"
            ],
            "cœur": [
                "bonheur",
                "chaleur",
                "douceur"
            ],
            "temps": [
                "printemps",
                "vent",
                "moment"
            ],
            "rêve": [
                "sève",
                "grève",
                "achève"
            ],
            "route": [
                "doute",
                "écoute",
                "voûte"
            ],
            "âme": [
                "flamme",
                "femme",
                "trame"
            ],
            "étoile": [
                "voile",
                "toile"
            ],
            "soleil": [
                "réveil",
                "merveille",
                "pareil"
            ],
            "vie": [
                "envie",
                "infini",
                "ainsi"
            ],
            "chemin": [
                "matin",
                "destin",
                "enfin"
            ]
        }

_ACROSTIC_SW = {
            "A": [
                "subuhi huleta matumaini mapya"
            ],
            "B": [
                "ahari hunong'ona siri zake"
            ],
            "C": [
                "hemchemi hutiririka bila kikomo"
            ],
            "D": [
                "unia hugeuka polepole kila siku"
            ],
            "E": [
                "limu hufungua milango mingi"
            ],
            "F": [
                "uraha hujificha kwenye vitu vidogo"
            ],
            "G": [
                "iza hupita, mwanga hufuata"
            ],
            "H": [
                "isia huja na kuondoka kama mawimbi"
            ],
            "I": [
                "mani husimama hata dhoruba ikivuma"
            ],
            "J": [
                "ua huchomoza tena kesho"
            ],
            "K": [
                "umbukumbu hubaki hata baada ya miaka"
            ],
            "L": [
                "engo huja kwa uvumilivu"
            ],
            "M": [
                "vua huleta uzima kwenye ardhi kavu"
            ],
            "N": [
                "yota huangaza hata gizani"
            ],
            "O": [
                "mbi la kweli halipotei"
            ],
            "P": [
                "endo halichoki kungoja"
            ],
            "Q": [
                " ni herufi nadra, lakini bado ina nafasi yake"
            ],
            "R": [
                "afiki wa kweli hubaki karibu"
            ],
            "S": [
                "afari ndefu huanza na hatua moja"
            ],
            "T": [
                "umaini huishi hata gizani"
            ],
            "U": [
                "pendo hauna mipaka"
            ],
            "V": [
                "umbi la jana huachwa nyuma"
            ],
            "W": [
                "imbo wa moyo huwa wa kweli daima"
            ],
            "X": [
                " ni ishara ya kile kisichojulikana bado"
            ],
            "Y": [
                "aliyopita hufundisha yajayo"
            ],
            "Z": [
                "awadi kubwa mara nyingi huwa ndogo"
            ]
        }

_ACROSTIC_FR = {
            "A": [
                "ube nouvelle apporte l'espoir"
            ],
            "B": [
                "rise légère chante doucement"
            ],
            "C": [
                "haque instant compte à sa façon"
            ],
            "D": [
                "ouceur du soir apaise l'âme"
            ],
            "E": [
                "toile filante porte un vœu"
            ],
            "F": [
                "eu qui danse réchauffe le cœur"
            ],
            "G": [
                "râce silencieuse guide nos pas"
            ],
            "H": [
                "orizon lointain appelle les rêveurs"
            ],
            "I": [
                "nstant présent mérite d'être vécu"
            ],
            "J": [
                "ardin secret garde ses couleurs"
            ],
            "K": [
                "aléidoscope de couleurs danse au vent"
            ],
            "L": [
                "umière douce traverse la fenêtre"
            ],
            "M": [
                "arée montante efface les traces"
            ],
            "N": [
                "uage passager cache le soleil"
            ],
            "O": [
                "mbre légère suit chaque pas"
            ],
            "P": [
                "luie fine murmure sur le toit"
            ],
            "Q": [
                "uiétude du soir enveloppe la ville"
            ],
            "R": [
                "êve oublié revient parfois"
            ],
            "S": [
                "ilence profond parle plus fort que les mots"
            ],
            "T": [
                "emps qui passe laisse des traces douces"
            ],
            "U": [
                "nivers infini garde ses mystères"
            ],
            "V": [
                "ent léger chuchote une chanson"
            ],
            "W": [
                "agon du souvenir avance lentement"
            ],
            "X": [
                "ylophone lointain résonne doucement"
            ],
            "Y": [
                "eux fermés, le cœur voit mieux"
            ],
            "Z": [
                "este de vie parfume chaque jour"
            ]
        }

_HAIKU_SW = {
            "1": [
                "theluji inaanguka polepole",
                "mto unatiririka kimya",
                "majani yanapeperushwa na upepo",
                "asubuhi inagusa vilima",
                "nyota zinameremeta juu",
                "mvua inagonga kioo",
                "mlango wa zamani unalia",
                "baridi inafunika shamba",
                "moshi unapaa kutoka motoni",
                "bwawa liko kimya kabisa",
                "jua linachomoza taratibu",
                "upepo unapita kimyakimya",
                "maua yanachanua asubuhi"
            ],
            "2": [
                "na ukimya unatawala kila kitu",
                "wakati bonde linashikilia pumzi",
                "mwanga mmoja gizani",
                "hakuna kinachosonga isipokuwa upepo",
                "msimu unabadilika tena",
                "na ukimya unajibu kwa upole",
                "vivuli vinajinyoosha njiani",
                "korongo linasubiri kwenye matete",
                "asubuhi inasubiri mlangoni",
                "dunia inapumua na kutulia",
                "na majani yanaanguka pole pole",
                "huku ndege wakiimba mbali",
                "wakati mvua inanyesha kimya"
            ],
            "3": [
                "mwezi unapanda angani",
                "maua yanagusa ardhi",
                "upepo unapita matete",
                "bustani sasa inalala",
                "mawimbi yanafika ufukweni",
                "nyota zinang'aa kimya",
                "jua linatua polepole",
                "ndege wanaruka mbali",
                "moto unawaka kimya kabisa",
                "theluji inafunika njia",
                "usiku unaingia taratibu"
            ]
        }

_HAIKU_FR = {
            "1": [
                "la neige tombe doucement",
                "la rivière coule lentement",
                "les feuilles dansent au vent",
                "le matin touche les collines",
                "les étoiles scintillent",
                "la pluie frappe la vitre",
                "la vieille porte grince",
                "le givre couvre le champ",
                "la fumée monte du feu",
                "l'étang reste immobile",
                "le soleil se lève doucement",
                "le vent passe en silence",
                "les fleurs s'ouvrent au matin"
            ],
            "2": [
                "et le silence s'installe",
                "pendant que la vallée retient son souffle",
                "une seule lumière dans le noir",
                "et rien ne bouge sauf le vent",
                "la saison tourne encore une fois",
                "et le silence répond doucement",
                "les ombres s'étirent le long du chemin",
                "un héron attend dans les roseaux",
                "le matin attend à la porte",
                "le monde expire et se calme",
                "et les feuilles tombent lentement",
                "tandis que les oiseaux chantent au loin",
                "pendant que la pluie tombe doucement"
            ],
            "3": [
                "la lune monte dans le ciel",
                "les pétales touchent le sol",
                "le vent traverse les roseaux",
                "le jardin dort maintenant",
                "les vagues atteignent la rive",
                "les étoiles brillent en silence",
                "le soleil se couche doucement",
                "les oiseaux s'envolent au loin",
                "le feu brûle en silence",
                "la neige couvre le chemin",
                "la nuit tombe doucement"
            ]
        }



class PoemWriter:
    """
    Generates poems using purely rule-based templates:
      - Acrostic poems (first letters spell a word, e.g. the user's name)
      - Haiku-style poems (5-7-5 syllable rule for English, approximated
        with a simple rule-based syllable counter - no ML, no dictionary
        lookups online; Swahili/French use a fixed, hand-checked line bank
        instead, since the English vowel-counting heuristic below doesn't
        model those languages' syllable/liaison rules)
      - Rhyming couplets (built from a small hand-written rhyme dictionary
        per language)

    None of this involves training or learning; it is template filling
    plus deterministic rules (syllable heuristics, rhyme lookups).
    """

    # Word banks, organized by theme, one per language (en/sw/fr) so the
    # acrostic and couplet generators can respond in whichever language
    # LanguageDetector identified, same idea as the Section 8 response
    # banks. Swahili and French word choices are separate translations,
    # not literal word-for-word substitutions, so the resulting lines
    # still read naturally in each language.
    _THEME_WORDS_EN = {
        "nature": ["forest", "river", "mountain", "ocean", "breeze", "meadow",
                   "sunlight", "thunder", "blossom", "stone", "horizon", "dew"],
        "love": ["heart", "warmth", "embrace", "longing", "gentle", "forever",
                 "tender", "devotion", "closeness", "softly", "cherish", "glow"],
        "time": ["moment", "memory", "tomorrow", "yesterday", "clockwork",
                 "fleeting", "patience", "season", "dawn", "twilight", "hour"],
        "space": ["galaxy", "starlight", "orbit", "comet", "nebula", "cosmos",
                  "gravity", "voyage", "infinite", "stardust", "meteor"],
        "general": ["wonder", "courage", "silence", "journey", "shadow",
                    "echo", "spark", "horizon", "wander", "quiet", "bright"],
        "friendship": ["laughter", "loyalty", "kindred", "trust", "company",
                       "steadfast", "warmth", "belonging", "shared", "together"],
        "seasons": ["harvest", "frost", "bloom", "monsoon", "solstice",
                    "evergreen", "thaw", "amber", "chill", "renewal"],
        "hope": ["dream", "tomorrow", "promise", "dawn", "faith", "light",
                 "rise", "courage", "chance", "horizon"],
    }

    THEME_WORDS = {"en": _THEME_WORDS_EN, "sw": _THEME_WORDS_SW, "fr": _THEME_WORDS_FR}

    # A small hand-written rhyme dictionary per language: word -> list of
    # words that rhyme with it. Deliberately small and explicit (rigid,
    # not learned). The Swahili and French banks use anchor words natural
    # to those languages rather than translating the English anchors.
    _RHYME_BANK_EN = {
        "light": ["night", "bright", "sight", "flight", "delight"],
        "night": ["light", "bright", "sight", "flight", "delight"],
        "day": ["away", "play", "stay", "ray", "gray"],
        "sea": ["free", "be", "tree", "key", "glee"],
        "heart": ["start", "part", "art", "apart"],
        "sky": ["high", "fly", "by", "why"],
        "rain": ["again", "pain", "remain", "plain", "chain"],
        "dream": ["stream", "gleam", "beam", "seem", "team"],
        "star": ["far", "are", "scar", "afar"],
        "moon": ["soon", "tune", "june", "balloon"],
        "shore": ["more", "before", "door", "explore"],
        "wind": ["pinned", "thinned", "skinned"],
        "fire": ["desire", "higher", "inspire", "tire"],
        "snow": ["glow", "grow", "slow", "below"],
        "friend": ["mend", "bend", "send", "defend"],
        "road": ["load", "bestowed", "flowed", "glowed"],
        "hope": ["scope", "slope", "rope", "cope"],
        "gold": ["bold", "told", "cold", "unfold"],
        "smile": ["mile", "while", "style", "worthwhile"],
        "eyes": ["skies", "rise", "surprise", "disguise"],
        "love": ["above", "dove", "glove", "shove"],
        "soul": ["whole", "goal", "role", "control"],
        "peace": ["release", "increase", "masterpiece"],
        "storm": ["warm", "form", "norm"],
        "grace": ["place", "space", "embrace", "trace"],
        "flame": ["name", "fame", "claim", "tame"],
        "song": ["long", "strong", "belong", "along"],
    }

    RHYME_BANK = {"en": _RHYME_BANK_EN, "sw": _RHYME_BANK_SW, "fr": _RHYME_BANK_FR}

    VOWELS = "aeiouy"

    # ---- syllable counting -------------------------------------------------

    def count_syllables(self, word: str) -> int:
        """
        A simple, rigid heuristic syllable counter (no dictionary lookup,
        no ML): count vowel groups, with a small correction for silent
        trailing 'e'. This is the same kind of heuristic widely used in
        rule-based text tools; it isn't perfectly accurate but is fast,
        deterministic, and fully offline. Tuned for English only - see
        the haiku() docstring for how Swahili/French sidestep this.
        """
        word = word.lower().strip(string.punctuation)
        if not word:
            return 0

        count = 0
        prev_was_vowel = False
        for ch in word:
            is_vowel = ch in self.VOWELS
            if is_vowel and not prev_was_vowel:
                count += 1
            prev_was_vowel = is_vowel

        if word.endswith("e") and count > 1 and not word.endswith("le"):
            count -= 1

        return max(count, 1)

    def count_line_syllables(self, line: str) -> int:
        words = re.findall(r"[a-zA-Z']+", line)
        return sum(self.count_syllables(w) for w in words)

    # ---- acrostic -----------------------------------------------------------

    def acrostic(self, word: str, lang: str = "en") -> str:
        """Build an acrostic poem where each line starts with successive
        letters of `word`, using theme-relevant phrase fragments in
        whichever of the three languages was requested."""
        word = re.sub(r"[^a-zA-Z]", "", word).upper()
        if not word:
            word = "HELLO"

        fragments_by_letter = self._build_letter_fragments(lang)
        fallback = {
            "en": "is a quiet wonder all its own",
            "sw": "ni ajabu ya kimya ya pekee yake",
            "fr": "est une merveille silencieuse à part entière",
        }.get(lang, "is a quiet wonder all its own")
        lines = []
        for letter in word:
            options = fragments_by_letter.get(letter)
            if options:
                fragment = random.choice(options)
            else:
                fragment = fallback
            lines.append(f"{letter}{fragment}")
        return "\n".join(lines)

    @staticmethod
    def _build_letter_fragments(lang: str = "en"):
        """A hand-written bank of line-completions keyed by starting letter,
        designed so the acrostic reads naturally regardless of the input
        word, in whichever language was requested."""
        en_fragments = {
            "A": ["lways reaching for the light", "wakens something deep inside", "ll at once, the quiet shifts"],
            "B": ["right as morning's first hour", "eyond the hills, a calm unfolds", "old enough to chase the dawn"],
            "C": ["arried gently on the breeze", "alm settles over everything", "limbing slowly toward the sun"],
            "D": ["rifting like a feather down", "ay breaks soft across the field", "eep within, a quiet spark"],
            "E": ["very moment holds a story", "choes linger in the dark", "ndless as the open sky"],
            "F": ["orever changing, never still", "ar beyond what eyes can see", "alling gently into place"],
            "G": ["entle as the evening tide", "rowing stronger every day", "lowing softly, warm and slow"],
            "H": ["olding fast to what remains", "ere, the silence speaks the loudest", "opeful even in the rain"],
            "I": ["nside, a thousand colors bloom", "magine all that's still to come", "n the stillness, something grows"],
            "J": ["ourneys further than they seem", "oy arrives without a warning", "ust beyond the next horizon"],
            "K": ["eeping every promise made", "ind words travel further still", "nown only to the patient heart"],
            "L": ["ight finds its way through every crack", "ingers longer than expected", "ooking forward, not behind"],
            "M": ["oves like water, finds its way", "akes a home in unlikely places", "orning always finds a way"],
            "N": ["ever quite the way it seemed", "othing stays exactly still", "ear enough to almost touch"],
            "O": ["pens slowly, like a door", "nce in every quiet while", "ut beyond the furthest edge"],
            "P": ["atience pays in ways unseen", "asses gently, hand to hand", "ainted soft in fading light"],
            "Q": ["uietly the answer comes", "uestions linger, unafraid", "uick as a passing thought"],
            "R": ["ises even after falling", "emembers everything it's lost", "eaches farther than it knows"],
            "S": ["tarts again with every breath", "oftly, surely, finds its place", "hines through every kind of weather"],
            "T": ["ravels farther than it planned", "ime forgives what time has broken", "ouches lightly, leaves a mark"],
            "U": ["nfolds in its own good time", "nderneath it all, still steady", "p ahead, the path grows clear"],
            "V": ["entures out beyond the known", "oices carry on the wind"],
            "W": ["anders without losing heart", "aits patiently for morning", "onders what the day will bring"],
            "X": [" marks a place still unexplored"],
            "Y": ["ields to nothing but the dawn", "earns for something just ahead"],
            "Z": ["ig-zags softly toward the light", "ero in on what remains"],
        }
        if lang == "sw":
            return _ACROSTIC_SW
        if lang == "fr":
            return _ACROSTIC_FR
        return en_fragments

    # ---- haiku ---------------------------------------------------------------

    HAIKU_LINE_BANK = {
        5: [
            "snow falls on the roof", "the river runs slow", "leaves drift on the wind",
            "morning finds the hills", "stars blink overhead", "rain taps on the glass",
            "the old door creaks shut", "frost covers the field", "smoke curls from the fire",
            "the pond sits so still", "petals touch the ground", "the moon climbs the sky",
            "wind moves through the reeds", "the garden sleeps now", "waves reach for the shore",
            "autumn wind blows on", "the candle burns low", "dawn breaks over hills",
            "cicadas sing loud", "cold wind stirs the field",
        ],
        7: [
            "and quiet settles in close", "while the valley holds its breath",
            "a single light in the dark", "and nothing moves but the wind",
            "the season turns once again", "and silence answers softly",
            "while shadows stretch down the lane", "a heron waits in the reeds",
            "and morning waits at the door", "the world exhales and grows still",
            "while distant thunder replies", "and the fields turn gold and gray",
            "and the lantern flickers twice", "the mountains stand watch alone",
            "beneath a blanket of frost", "a heron lifts from the marsh",
            "the harvest moon climbs slowly",
        ],
    }

    # Swahili/French haiku-style line pools, keyed by line position
    # (1/2/3) rather than syllable count - see the haiku() docstring for
    # why these bypass the English syllable heuristic entirely.
    HAIKU_LINE_BANK_SW = _HAIKU_SW
    HAIKU_LINE_BANK_FR = _HAIKU_FR

    def haiku(self, topic: str = None, lang: str = "en") -> str:
        """
        Build a 3-line haiku-style poem. For English this follows the
        classic 5-7-5 syllable rule, with lines assembled from a
        hand-written bank and verified against the rule-based syllable
        counter, plus an optional topic word woven into the first line
        when it fits cleanly. For Swahili and French, syllable counting
        with an English-tuned vowel heuristic isn't linguistically valid
        (different vowel/liaison rules), so those two languages instead
        draw from their own fixed, hand-checked 3-line pools - still
        template filling, just without the syllable-count verification
        step that only makes sense for English.
        """
        if lang == "sw":
            pool = self.HAIKU_LINE_BANK_SW
            return f"{random.choice(pool['1'])}\n{random.choice(pool['2'])}\n{random.choice(pool['3'])}"
        if lang == "fr":
            pool = self.HAIKU_LINE_BANK_FR
            return f"{random.choice(pool['1'])}\n{random.choice(pool['2'])}\n{random.choice(pool['3'])}"

        line1_options = list(self.HAIKU_LINE_BANK[5])
        line2_options = list(self.HAIKU_LINE_BANK[7])
        line3_options = list(self.HAIKU_LINE_BANK[5])

        if topic:
            topic_clean = re.sub(r"[^a-zA-Z\s]", "", topic).strip().lower()
            if topic_clean:
                syl = self.count_syllables(topic_clean.split()[0])
                if syl <= 3:
                    candidate = f"{topic_clean} in the light"
                    if self.count_line_syllables(candidate) == 5:
                        line1_options.insert(0, candidate)

        line1 = random.choice(line1_options)
        line2 = random.choice(line2_options)
        line3 = random.choice(line3_options)

        # Verify syllable counts; if our heuristic disagrees (rare, given
        # the bank was hand-checked), fall back to safe defaults.
        if self.count_line_syllables(line1) != 5:
            line1 = "snow falls on the roof"
        if self.count_line_syllables(line2) != 7:
            line2 = "and quiet settles in close"
        if self.count_line_syllables(line3) != 5:
            line3 = "stars blink overhead"

        # Avoid the (visually awkward) case where line 1 and line 3 end up
        # being the exact same line - this can happen either from the
        # random pick above (both pools share the same 5-syllable bank)
        # or from both lines independently hitting the same syllable
        # fallback string, so this check must run AFTER the fallback logic
        # above, not before it.
        if line3 == line1:
            alternatives = [l for l in self.HAIKU_LINE_BANK[5] if l != line1]
            if alternatives:
                line3 = random.choice(alternatives)

        return f"{line1}\n{line2}\n{line3}"

    # ---- rhyming couplets -----------------------------------------------------

    @staticmethod
    def _article_for(word: str, lang: str = "en") -> str:
        """Return 'an'/'a' (English), or the appropriate short lead-in for
        Swahili/French. Swahili nouns don't take an indefinite article at
        all, so this returns an empty string for "sw". French distinguishes
        "un"/"une" by grammatical gender, which a first-letter heuristic
        can't determine correctly, so a neutral "un/une" placeholder is
        avoided in favor of just using "un" (the far more common case
        across this word bank's simple nouns) - a small, acknowledged
        simplification, not a full grammatical-gender model."""
        if lang == "sw":
            return ""
        if lang == "fr":
            return "un"
        return "an" if word and word[0].lower() in "aeiou" else "a"

    def rhyming_couplets(self, theme: str = "general", num_couplets: int = 2, lang: str = "en") -> str:
        """Build a short rhyming poem (AABB pattern) from the rhyme bank
        and theme word list for whichever language was requested."""
        theme_words_all = self.THEME_WORDS.get(lang, self.THEME_WORDS["en"])
        theme = theme.lower().strip()
        if theme not in theme_words_all:
            theme = "general"
        words = theme_words_all[theme]

        rhyme_bank = self.RHYME_BANK.get(lang, self.RHYME_BANK["en"])
        rhyme_anchors = list(rhyme_bank.keys())
        random.shuffle(rhyme_anchors)

        templates = {
            "en": lambda w1, article1, anchor, article2, w2, partner:
                (f"The {w1} calls where {article1} {anchor} may be,",
                 f"{article2} {w2} answers, wild and free, like {partner} drifting endlessly."),
            "sw": lambda w1, article1, anchor, article2, w2, partner:
                (f"{w1.capitalize()} huita mahali {anchor} inapoweza kuwa,",
                 f"{w2.capitalize()} hujibu, huru na bila mipaka, kama {partner} ikielea milele."),
            "fr": lambda w1, article1, anchor, article2, w2, partner:
                (f"Le {w1} appelle là où {article1} {anchor} pourrait être,",
                 f"{article2.capitalize()} {w2} répond, libre et sans limites, comme {partner} qui dérive à jamais."),
        }
        template = templates.get(lang, templates["en"])

        fallback = {
            "en": ["The world keeps turning, soft and slow,", "a quiet rhythm only hearts may know."],
            "sw": ["Dunia inaendelea kuzunguka, kwa upole na polepole,", "mdundo wa kimya ambao ni mioyo tu inayoujua."],
            "fr": ["Le monde continue de tourner, doux et lent,", "un rythme discret que seuls les cœurs comprennent."],
        }.get(lang, ["The world keeps turning, soft and slow,", "a quiet rhythm only hearts may know."])

        lines = []
        for i in range(num_couplets):
            if i >= len(rhyme_anchors):
                break
            anchor = rhyme_anchors[i]
            partner = random.choice(rhyme_bank[anchor])
            w1 = random.choice(words)
            w2 = random.choice(words)
            article1 = self._article_for(anchor, lang)
            article2 = self._article_for(w2, lang)
            line_a, line_b = template(w1, article1, anchor, article2, w2, partner)
            lines.append(line_a)
            lines.append(line_b)

        if not lines:
            return "\n".join(fallback)
        return "\n".join(lines)

    # Multiple couplet SHAPES per language (not just one), used by
    # full_page_poem() below so a long, multi-stanza poem doesn't just
    # repeat the exact same sentence structure over and over - the
    # template cycles between calls, only the theme word / rhyme pair
    # actually varies within rhyming_couplets() above.
    _FULL_POEM_TEMPLATES_EN = [
        lambda w1, article1, anchor, article2, w2, partner:
            (f"The {w1} calls where {article1} {anchor} may be,",
             f"{article2} {w2} answers, wild and free, like {partner} drifting endlessly."),
        lambda w1, article1, anchor, article2, w2, partner:
            (f"Beneath {article1} {anchor}, {article2} {w2} waits,",
             f"the {w1} watches on, like {partner}, past the gates."),
        lambda w1, article1, anchor, article2, w2, partner:
            (f"Where {article1} {anchor} meets the edge of {w1},",
             f"{article2} {w2} lingers still, like {partner} settling in."),
        lambda w1, article1, anchor, article2, w2, partner:
            (f"{w1.capitalize()} and {anchor}, side by side they stay,",
             f"{article2} {w2} drifts on, like {partner}, far away."),
    ]
    _FULL_POEM_TEMPLATES_SW = [
        lambda w1, article1, anchor, article2, w2, partner:
            (f"{w1.capitalize()} huita mahali {anchor} inapoweza kuwa,",
             f"{w2.capitalize()} hujibu, huru na bila mipaka, kama {partner} ikielea milele."),
        lambda w1, article1, anchor, article2, w2, partner:
            (f"Karibu na {anchor}, {w2} inasubiri kimya,",
             f"{w1} inatazama, kama {partner}, ikiwa mbali."),
    ]
    _FULL_POEM_TEMPLATES_FR = [
        lambda w1, article1, anchor, article2, w2, partner:
            (f"Le {w1} appelle là où {article1} {anchor} pourrait être,",
             f"{article2.capitalize()} {w2} répond, libre et sans limites, comme {partner} qui dérive à jamais."),
        lambda w1, article1, anchor, article2, w2, partner:
            (f"Près de {anchor}, {w2} attend en silence,",
             f"{w1.capitalize()} observe, comme {partner}, dans la distance."),
    ]
    _FULL_POEM_TEMPLATES = {
        "en": _FULL_POEM_TEMPLATES_EN,
        "sw": _FULL_POEM_TEMPLATES_SW,
        "fr": _FULL_POEM_TEMPLATES_FR,
    }

    def full_page_poem(self, theme: str = "general", lang: str = "en", num_stanzas: int = 6) -> str:
        """
        A 'full-page' poem: num_stanzas stanzas of 2 rhyming couplets
        (4 lines) each, separated by blank lines. Built the same way as
        rhyming_couplets() - same rhyme bank, same theme word list - but
        CYCLING through several different template shapes (see
        _FULL_POEM_TEMPLATES above) so a long poem doesn't read like the
        same sentence copy-pasted a dozen times, and reusing rhyme
        anchors (reshuffled) once the bank runs out rather than cutting
        the poem short - relevant for Swahili/French, whose rhyme banks
        are smaller than English's.
        """
        theme_words_all = self.THEME_WORDS.get(lang, self.THEME_WORDS["en"])
        theme = theme.lower().strip()
        if theme not in theme_words_all:
            theme = "general"
        words = theme_words_all[theme]

        rhyme_bank = self.RHYME_BANK.get(lang, self.RHYME_BANK["en"])
        rhyme_anchors = list(rhyme_bank.keys())
        if not rhyme_anchors:
            return self.rhyming_couplets(theme=theme, num_couplets=2, lang=lang)
        random.shuffle(rhyme_anchors)

        templates = self._FULL_POEM_TEMPLATES.get(lang, self._FULL_POEM_TEMPLATES["en"])
        template_order = list(range(len(templates)))

        stanzas = []
        anchor_i = 0
        last_template_i = -1
        for _stanza in range(max(1, num_stanzas)):
            stanza_lines = []
            for _couplet in range(2):
                if anchor_i >= len(rhyme_anchors):
                    random.shuffle(rhyme_anchors)
                    anchor_i = 0
                anchor = rhyme_anchors[anchor_i]
                anchor_i += 1
                partner = random.choice(rhyme_bank[anchor])
                w1 = random.choice(words)
                w2 = random.choice(words)
                article1 = self._article_for(anchor, lang)
                article2 = self._article_for(w2, lang)

                choices = [i for i in template_order if i != last_template_i] or template_order
                template_i = random.choice(choices)
                last_template_i = template_i
                line_a, line_b = templates[template_i](w1, article1, anchor, article2, w2, partner)
                stanza_lines.append(line_a)
                stanza_lines.append(line_b)
            stanzas.append("\n".join(stanza_lines))

        return "\n\n".join(stanzas)

# ==============================================================================
