#!/usr/bin/env python3
"""Generate every Little Lilies page from the shared chrome.

    python3 scripts/build-pages.py

Content rules this file obeys, taken from the marketing strategy:
  * only facts the school has confirmed in writing appear as statements;
  * anything outstanding is wrapped in .gate so it cannot ship by accident;
  * the forbidden claims ("best preschool", "full English medium",
    "government approved", "limited spaces") appear nowhere.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from chrome import head, header, footer, page_hero, CTA_BAND

ROOT = pathlib.Path(__file__).resolve().parent.parent
S = "                "

def card(icon, title, body, cls="u-card p-7"):
    return f"""<div class="{cls}">
                <span class="material-symbols-outlined text-primary !text-[30px]">{icon}</span>
                <h3 class="font-headline-md text-xl font-bold text-on-surface mt-3">{title}</h3>
                <p class="mt-2 font-body-md text-sm text-on-surface-variant">{body}</p>
            </div>"""

def section(inner, cls="py-section-padding-mobile md:py-section-padding-desktop", extra=""):
    return f'\n<section class="{cls}"{extra}>\n    <div class="mx-auto max-w-container-max px-gutter">\n{inner}\n    </div>\n</section>\n'

def heading(eyebrow, title, lede=None, center=False):
    al = "text-center max-w-[54ch] mx-auto" if center else "max-w-[48ch]"
    l = f'\n            <p class="mt-5 font-body-lg text-body-lg text-on-surface-variant">{lede}</p>' if lede else ""
    return f"""        <div class="{al}">
            <p class="font-label-bold text-label-bold text-error uppercase tracking-wider mb-3">{eyebrow}</p>
            <h2 class="font-headline-lg text-headline-lg-mobile md:text-headline-lg text-on-surface">{title}</h2>{l}
        </div>"""

PAGES = {}

# ---------------------------------------------------------------- ABOUT ----
PAGES["about.html"] = dict(
    title="About Little Lilies Pre-School | Mogoditshane",
    desc="Little Lilies is a new preschool in Mogoditshane, Botswana, for children two and a half to five years. Structured early learning, daily English and a caring environment.",
    hero=("About us", "A small school, built around one promise",
          "Little Lilies is new. That means we cannot point to decades of history, so instead we "
          "invite you to look closely at what we actually do every day."),
    body=(
        section(heading("What we are for",
                        "Quality early education, made reachable",
                        "Little Lilies is a nurturing preschool combining structured early learning with daily "
                        "English development in a caring environment, making quality early childhood education "
                        "accessible to families in Mogoditshane.")
                + """
        <div class="mt-12 grid md:grid-cols-3 gap-6">
            """ + card("school", "Structured learning",
                       "A clear daily routine that combines guided learning with purposeful play, so children always know what comes next.")
                + "\n            " + card("record_voice_over", "Daily English",
                       "Stories, songs, vocabulary and conversation woven through the whole day, rather than taught in a single slot.")
                + "\n            " + card("volunteer_activism", "A caring environment",
                       "Small enough that every child is known by name, and every parent can speak to someone who knows them.")
                + """
        </div>""")
        + section(heading("Why parents choose us", "Six things we will hold ourselves to")
                  + """
        <div class="mt-12 grid md:grid-cols-2 gap-x-14 gap-y-0">
            <div class="divide-y divide-outline-variant">
                <div class="py-6"><p class="font-label-bold text-label-bold text-error uppercase tracking-wider">01</p><h3 class="font-headline-md text-xl font-bold text-on-surface mt-1.5">Structured daily learning</h3><p class="mt-2 font-body-md text-sm text-on-surface-variant">A clear routine combining guided learning and purposeful play.</p></div>
                <div class="py-6"><p class="font-label-bold text-label-bold text-error uppercase tracking-wider">02</p><h3 class="font-headline-md text-xl font-bold text-on-surface mt-1.5">Daily English development</h3><p class="mt-2 font-body-md text-sm text-on-surface-variant">Stories, songs, vocabulary and conversation that build confidence.</p></div>
                <div class="py-6"><p class="font-label-bold text-label-bold text-error uppercase tracking-wider">03</p><h3 class="font-headline-md text-xl font-bold text-on-surface mt-1.5">Strong school readiness</h3><p class="mt-2 font-body-md text-sm text-on-surface-variant">Communication, early concepts, routines and social confidence.</p></div>
            </div>
            <div class="divide-y divide-outline-variant">
                <div class="py-6"><p class="font-label-bold text-label-bold text-error uppercase tracking-wider">04</p><h3 class="font-headline-md text-xl font-bold text-on-surface mt-1.5">Caring teachers</h3><p class="mt-2 font-body-md text-sm text-on-surface-variant">Real teachers whose warmth, roles and experience are visible to you.</p></div>
                <div class="py-6"><p class="font-label-bold text-label-bold text-error uppercase tracking-wider">05</p><h3 class="font-headline-md text-xl font-bold text-on-surface mt-1.5">A safe, clean environment</h3><p class="mt-2 font-body-md text-sm text-on-surface-variant">Shown to you on a visit, rather than described in a brochure.</p></div>
                <div class="py-6"><p class="font-label-bold text-label-bold text-error uppercase tracking-wider">06</p><h3 class="font-headline-md text-xl font-bold text-on-surface mt-1.5">Affordable payment options</h3><p class="mt-2 font-body-md text-sm text-on-surface-variant">Clear fees and instalments that local families can plan around.</p></div>
            </div>
        </div>""", cls="py-section-padding-mobile md:py-section-padding-desktop bg-surface-container-low rounded-xl mx-4 md:mx-8 my-12 shadow-sm")
        + section(heading("Our teachers", "The people who will know your child", center=True)
                  + """
        <div class="mt-12 grid sm:grid-cols-4 gap-6">
            <div class="feature-card bg-white rounded p-6 text-center transition-shadow duration-300"><img src="img/school/teacher-1.jpg" alt="A member of the Little Lilies teaching team" class="rounded-full shadow-lg w-32 h-32 mx-auto object-cover"/><p class="mt-5 font-body-md text-sm text-outline gate inline-block px-3">Name and role to confirm</p></div>
            <div class="feature-card bg-white rounded p-6 text-center transition-shadow duration-300"><img src="img/school/teacher-2.jpg" alt="A member of the Little Lilies teaching team" class="rounded-full shadow-lg w-32 h-32 mx-auto object-cover"/><p class="mt-5 font-body-md text-sm text-outline gate inline-block px-3">Name and role to confirm</p></div>
            <div class="feature-card bg-white rounded p-6 text-center transition-shadow duration-300"><img src="img/school/teacher-3.jpg" alt="A member of the Little Lilies teaching team" class="rounded-full shadow-lg w-32 h-32 mx-auto object-cover"/><p class="mt-5 font-body-md text-sm text-outline gate inline-block px-3">Name and role to confirm</p></div>
            <div class="feature-card bg-white rounded p-6 text-center transition-shadow duration-300"><img src="img/school/teacher-4.jpg" alt="A member of the Little Lilies teaching team" class="rounded-full shadow-lg w-32 h-32 mx-auto object-cover"/><p class="mt-5 font-body-md text-sm text-outline gate inline-block px-3">Name and role to confirm</p></div>
        </div>
        <img src="img/school/team-outdoors.jpg" alt="The Little Lilies teaching team outside the school" class="mt-10 leaf w-full max-h-[420px] object-cover shadow-md"/>
        </div>""")
        + CTA_BAND
    ),
)

# ----------------------------------------------------------- PROGRAMMES ----
PAGES["programs.html"] = dict(
    title="Programmes | Little Lilies Pre-School",
    desc="Little Lilies takes children from two and a half to five years in Mogoditshane. Structured play-based learning with daily English development.",
    hero=("Programmes", "From two and a half, to the year before big school",
          "We take children from two and a half to five years, from the first steps into a routine "
          "through to the confidence a child needs on their first day of primary school."),
    body=(
        section(heading("How the day is built", "Guided learning, purposeful play, English throughout",
                        "Our Botswana-aligned early-learning programme uses structured play and guided activities "
                        "to build school-readiness skills, with daily English stories, songs, vocabulary and "
                        "conversation.")
                + """
        <div class="mt-12 grid md:grid-cols-3 gap-6">
            """ + card("target", "Guided", "Adult-led activities that introduce early concepts in small groups.")
                + "\n            " + card("toys", "Play", "Purposeful play where children practise what they have just met.")
                + "\n            " + card("chat", "Language", "English woven through the whole day, not taught in a slot.")
                + """
        </div>""")
        + section(heading("Our groups", "How the age range is arranged", center=True)
                  + """
        <div class="mt-12 gate">
            <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">
                <div class="feature-card bg-white rounded p-6 transition-shadow duration-300"><p class="font-label-bold text-label-bold text-error uppercase tracking-wider">Age band to confirm</p><h3 class="font-headline-md text-xl font-bold text-on-surface mt-2">Group one</h3><p class="mt-2 font-body-md text-sm text-on-surface-variant">Ages, routine and group size awaiting written confirmation.</p></div>
                <div class="feature-card bg-white rounded p-6 transition-shadow duration-300"><p class="font-label-bold text-label-bold text-error uppercase tracking-wider">Age band to confirm</p><h3 class="font-headline-md text-xl font-bold text-on-surface mt-2">Group two</h3><p class="mt-2 font-body-md text-sm text-on-surface-variant">Ages, routine and group size awaiting written confirmation.</p></div>
                <div class="feature-card bg-white rounded p-6 transition-shadow duration-300"><p class="font-label-bold text-label-bold text-error uppercase tracking-wider">Age band to confirm</p><h3 class="font-headline-md text-xl font-bold text-on-surface mt-2">Group three</h3><p class="mt-2 font-body-md text-sm text-on-surface-variant">Ages, routine and group size awaiting written confirmation.</p></div>
                <div class="feature-card bg-white rounded p-6 transition-shadow duration-300"><p class="font-label-bold text-label-bold text-error uppercase tracking-wider">Age band to confirm</p><h3 class="font-headline-md text-xl font-bold text-on-surface mt-2">Group four</h3><p class="mt-2 font-body-md text-sm text-on-surface-variant">Ages, routine and group size awaiting written confirmation.</p></div>
            </div>
        </div>
        <p class="mt-6 font-body-md text-sm text-outline text-center max-w-[56ch] mx-auto">We take children from two and a half to five. Exactly how that range is divided into groups is being confirmed with the school, and this page will be updated as soon as it is.</p>""",
                  cls="py-section-padding-mobile md:py-section-padding-desktop bg-surface-container-low rounded-xl mx-4 md:mx-8 my-12 shadow-sm")
        + section(heading("A day in the life", "See the whole day", center=True,
                          lede="The homepage walks you through a full day at Little Lilies, from the goodbye at the gate to the moment you come back for them.")
                  + """
        <img src="img/school/classroom-tables.jpg" alt="Child-height tables set for small-group work at Little Lilies" class="mt-10 leaf w-full max-h-[380px] object-cover shadow-md"/>
        <div class="mt-10 text-center">
            <a href="index.html#our-day" class="inline-flex items-center gap-2 bg-primary-container text-on-primary-container py-4 px-8 rounded-full font-label-bold text-label-bold hover:scale-105 transition-colors">
                Walk through our day
            </a>
        </div>""")
        + CTA_BAND
    ),
)

# ----------------------------------------------------------- ADMISSIONS ----
DOCS = [
    ("little-lilies-prospectus.pdf", "auto_stories",     "Prospectus",         "Who we are and how the day works."),
    ("enrolment-form.pdf",           "edit_document",    "Enrolment form",     "Your child's details and who may collect them."),
    ("medical-consent-form.pdf",     "health_and_safety","Medical &amp; consent","Allergies, dietary needs and permissions."),
    ("fee-sheet.pdf",                "payments",         "Fee sheet",          "Fees, instalments and how to pay."),
    ("parent-handbook.pdf",          "menu_book",        "Parent handbook",    "Our routines and how we keep in touch."),
]
doc_cards = "\n".join(
    f"""            <li><a href="docs/{f}" download class="feature-card bg-white rounded p-6 flex flex-col h-full transition-shadow duration-300">
                <span class="material-symbols-outlined text-primary !text-[30px]">{i}</span>
                <span class="font-headline-md text-xl font-bold text-on-surface mt-3">{t}</span>
                <span class="mt-2 font-body-md text-sm text-on-surface-variant flex-1">{d}</span>
                <span class="mt-5 text-body-sm font-semibold text-primary flex items-center gap-1.5">
                    <span class="material-symbols-outlined !text-[17px]">download</span> PDF</span></a></li>"""
    for f, i, t, d in DOCS)

STEPS = [
    ("Ask us a question", "Send an enquiry, call, or message us on WhatsApp. Tell us your child's age and where you live."),
    ("Come and visit", "We will suggest some times. Bring your child if you can, how they respond to the room tells you a lot."),
    ("Complete the forms", "The enrolment form and the medical and consent form. Both are on this page to print and bring with you."),
    ("Confirm the place", "A place is confirmed once the registration fee is received and we have confirmed it to you in writing."),
]
step_html = "\n".join(
    f"""            <li class="flex gap-5">
                <span class="shrink-0 w-10 h-10 rounded-full bg-surface-container text-primary font-display font-semibold grid place-items-center">{n+1}</span>
                <div><h3 class="font-headline-md text-xl font-bold text-on-surface">{t}</h3>
                <p class="mt-1.5 font-body-md text-sm text-on-surface-variant max-w-[52ch]">{b}</p></div>
            </li>""" for n, (t, b) in enumerate(STEPS))

PAGES["admissions.html"] = dict(
    title="Admissions &amp; Fees | Little Lilies Pre-School",
    desc="Little Lilies Pre-School fees: P5,100 per term including food, or three instalments of P1,700. Registration P200. Download the enrolment forms.",
    hero=("Admissions", "Clear fees, written down",
          "No surprises and no numbers that change later. Here is what it costs, what it covers, and "
          "exactly how to join us."),
    body=(
        section("""        <div class="grid lg:grid-cols-[1.15fr_.85fr] gap-6">
            <div class="feature-card bg-white rounded p-8">
                <h2 class="font-headline-md text-headline-md text-on-surface">Fees</h2>
                <p class="mt-2 font-body-md text-sm text-outline">All amounts in Botswana Pula, per child. Food is included.</p>
                <dl class="mt-8 divide-y divide-outline-variant">
                    <div class="flex justify-between items-baseline gap-5 pb-5">
                        <dt class="text-body-lg font-semibold">School fees, per term</dt>
                        <dd class="font-display text-[30px] font-semibold text-primary whitespace-nowrap">P5,100</dd></div>
                    <div class="flex justify-between items-baseline gap-5 py-4">
                        <dt class="font-body-md text-sm text-on-surface-variant">Or three instalments of<br/><span class="text-outline">First payment, second payment, final payment</span></dt>
                        <dd class="font-display text-[21px] font-semibold text-foreground whitespace-nowrap">P1,700</dd></div>
                    <div class="flex justify-between items-baseline gap-5 py-4">
                        <dt class="font-body-md text-sm text-on-surface-variant">Registration<br/><span class="text-outline">Once off, non-refundable</span></dt>
                        <dd class="font-display text-[21px] font-semibold text-foreground whitespace-nowrap">P200</dd></div>
                    <div class="flex justify-between items-baseline gap-5 pt-4">
                        <dt class="font-body-md text-sm text-on-surface-variant">DAV fee<br/><span class="text-outline">P400 first payment, P400 second payment</span></dt>
                        <dd class="font-display text-[21px] font-semibold text-foreground whitespace-nowrap">P800</dd></div>
                </dl>
            </div>
            <div class="grid gap-6 content-start">
                <div class="feature-card bg-white rounded p-6">
                    <span class="material-symbols-outlined text-primary !text-[32px]">child_care</span>
                    <h3 class="font-headline-md text-xl font-bold text-on-surface mt-3">Who we take</h3>
                    <p class="mt-2 font-body-md text-sm text-on-surface-variant">Children from <strong class="text-foreground">two and a half to five years</strong>.</p>
                </div>
                <div class="feature-card bg-white rounded p-6">
                    <span class="material-symbols-outlined text-primary !text-[32px]">restaurant</span>
                    <h3 class="font-headline-md text-xl font-bold text-on-surface mt-3">Food included</h3>
                    <p class="mt-2 font-body-md text-sm text-on-surface-variant">Meals are part of the term fee, not an extra charge.</p>
                </div>
                <div class="feature-card bg-white rounded p-6 gate">
                    <span class="material-symbols-outlined text-secondary !text-[32px]">schedule</span>
                    <h3 class="font-headline-md text-xl font-bold text-on-surface mt-3">Hours &amp; sessions</h3>
                    <p class="mt-2 font-body-md text-sm text-on-surface-variant">Opening, collection and session times are being confirmed with the school.</p>
                </div>
            </div>
        </div>""")
        + section(heading("How to join", "Four steps, and most families finish in one visit")
                  + f"""
        <ol class="mt-12 grid md:grid-cols-2 gap-x-14 gap-y-9">
{step_html}
        </ol>""", cls="py-section-padding-mobile md:py-section-padding-desktop bg-surface-container-low rounded-xl mx-4 md:mx-8 my-12 shadow-sm")
        + section(heading("Take it with you", "Everything you need, on paper",
                          lede="Read them before you come, or print the forms and bring them with you.")
                  + f"""
        <ul class="mt-12 grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
{doc_cards}
        </ul>""", extra=' id="downloads"')
        + CTA_BAND
    ),
)

# -------------------------------------------------------------- GALLERY ----
PAGES["gallery.html"] = dict(
    title="Gallery | Little Lilies Pre-School",
    desc="Photographs of Little Lilies Pre-School in Mogoditshane, our classrooms, playground, learning displays and the team who will look after your child.",
    hero=("Gallery", "See the actual school",
          "Not stock photographs of somebody else's preschool. These are our rooms, our playground "
          "and our team, as they are."),
    body=(
        section("""        <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-x-8 gap-y-12">
            <figure><img src="img/school/exterior-front.jpg" alt="The front of the school at Little Lilies Pre-School" class="rounded shadow-lg w-full aspect-[4/5] object-cover"/>
                <figcaption class="mt-4 text-center font-body-md text-sm text-on-surface-variant">The front of the school</figcaption></figure>
            <figure><img src="img/school/playground-wide.jpg" alt="The playground at Little Lilies Pre-School" class="rounded shadow-lg w-full aspect-[4/5] object-cover"/>
                <figcaption class="mt-4 text-center font-body-md text-sm text-on-surface-variant">The playground</figcaption></figure>
            <figure><img src="img/school/classroom-wide.jpg" alt="A classroom at Little Lilies Pre-School" class="rounded shadow-lg w-full aspect-[4/5] object-cover"/>
                <figcaption class="mt-4 text-center font-body-md text-sm text-on-surface-variant">A classroom</figcaption></figure>
            <figure><img src="img/school/classroom-tables.jpg" alt="Where small groups work at Little Lilies Pre-School" class="rounded shadow-lg w-full aspect-[4/5] object-cover"/>
                <figcaption class="mt-4 text-center font-body-md text-sm text-on-surface-variant">Where small groups work</figcaption></figure>
            <figure><img src="img/school/reading-corner.jpg" alt="The reading shelves at Little Lilies Pre-School" class="rounded shadow-lg w-full aspect-[4/5] object-cover"/>
                <figcaption class="mt-4 text-center font-body-md text-sm text-on-surface-variant">The reading shelves</figcaption></figure>
            <figure><img src="img/school/letters-wall.jpg" alt="The alphabet wall at Little Lilies Pre-School" class="rounded shadow-lg w-full aspect-[4/5] object-cover"/>
                <figcaption class="mt-4 text-center font-body-md text-sm text-on-surface-variant">The alphabet wall</figcaption></figure>
            <figure><img src="img/school/playground.jpg" alt="Climbing and swings at Little Lilies Pre-School" class="rounded shadow-lg w-full aspect-[4/5] object-cover"/>
                <figcaption class="mt-4 text-center font-body-md text-sm text-on-surface-variant">Climbing and swings</figcaption></figure>
            <figure><img src="img/school/classroom-charts.jpg" alt="Learning displays at Little Lilies Pre-School" class="rounded shadow-lg w-full aspect-[4/5] object-cover"/>
                <figcaption class="mt-4 text-center font-body-md text-sm text-on-surface-variant">Learning displays</figcaption></figure>
            <figure><img src="img/school/exterior-gate.jpg" alt="The gate and yard at Little Lilies Pre-School" class="rounded shadow-lg w-full aspect-[4/5] object-cover"/>
                <figcaption class="mt-4 text-center font-body-md text-sm text-on-surface-variant">The gate and yard</figcaption></figure>
        </div>""")
        + section("""        <div class="feature-card bg-white rounded p-8 text-center max-w-[64ch] mx-auto">
            <span class="material-symbols-outlined text-tertiary !text-[34px]">photo_camera</span>
            <h2 class="font-headline-md text-headline-md text-on-surface mt-3">About photographs of children</h2>
            <p class="mt-3 font-body-lg text-body-lg text-on-surface-variant">We only publish photographs in which children cannot be identified, unless their parent has given us written permission. If you would like your child included, or removed, just tell us.</p>
            <a href="contact.html" class="mt-7 inline-flex items-center bg-primary-container text-on-primary-container py-4 px-8 rounded-full font-label-bold text-label-bold hover:scale-105 transition-colors">Come and see it in person</a>
        </div>""", cls="py-section-padding-mobile md:py-section-padding-desktop bg-surface-container-low rounded-xl mx-4 md:mx-8 my-12 shadow-sm")
        + CTA_BAND
    ),
)

# ------------------------------------------------------------------ FAQ ----
FAQS = [
    ("What ages do you take?",
     "Children from two and a half to five years, from settling into a routine through to the year before primary school."),
    ("What does the fee cover?",
     "P5,100 per term covers school fees and food. You can pay it in three instalments of P1,700 instead. Registration is P200 once off, and there is a DAV fee of P800 paid as P400 and P400."),
    ("Can I pay in instalments?",
     "Yes. Three payments of P1,700 rather than the full term fee up front. We agree the dates with you when you register."),
    ("Is food really included?",
     "Yes, meals are part of the term fee, not an extra charge. Tell us about any allergies or dietary needs on the medical and consent form."),
    ("Do you teach in English?",
     "English runs through the whole day, stories, songs, vocabulary and conversation, as part of a Botswana-aligned early-learning programme, rather than as a separate lesson."),
    ("Does registering hold a place?",
     "Not on its own. A place is confirmed once we have received the registration fee and have confirmed it to you in writing."),
    ("Can I visit before deciding?",
     "Please do. It is the only way to really judge a school. Send us a note or a WhatsApp message and we will suggest some times."),
    ("Where exactly are you?",
     "Plot 17051, Kgosing Ward, Mogoditshane. Call or WhatsApp us on +267 73 674 494 and we will help you find it."),
]
faq_html = "\n".join(
    f"""            <details class="u-card p-6 group">
                <summary class="flex items-center justify-between gap-4 cursor-pointer list-none">
                    <span class="font-headline-md text-xl font-bold text-on-surface">{q}</span>
                    <span class="material-symbols-outlined text-primary !text-[24px] transition-transform group-open:rotate-45 shrink-0">add</span>
                </summary>
                <p class="mt-3 font-body-md text-sm text-on-surface-variant max-w-2xl">{a}</p>
            </details>""" for q, a in FAQS)

PAGES["faq.html"] = dict(
    title="Frequently Asked Questions | Little Lilies Pre-School",
    desc="Answers to the questions parents ask most about Little Lilies Pre-School in Mogoditshane, ages, fees, instalments, meals, English and visiting.",
    hero=("Questions", "The things parents actually ask",
          "If your question is not here, ask us. We would rather answer it now than have you wonder."),
    body=(
        section(f"""        <div class="grid gap-4 max-w-[68ch] mx-auto">
{faq_html}
        </div>
        <div class="mt-10 text-center gate max-w-[62ch] mx-auto p-6">
            <p class="font-body-md text-sm text-on-surface-variant">Opening hours, collection times and group sizes will be added here once the school has confirmed them.</p>
        </div>""")
        + CTA_BAND
    ),
)

# -------------------------------------------------------------- CONTACT ----
PAGES["contact.html"] = dict(
    title="Contact &amp; Visit | Little Lilies Pre-School, Mogoditshane",
    desc="Visit Little Lilies Pre-School at Plot 17051, Kgosing Ward, Mogoditshane. Call or WhatsApp +267 73 674 494, or send an enquiry.",
    hero=("Contact", "Come and see us",
          "Send a short note and we will reply with some times to visit. It takes less than a minute."),
    body=(
        section("""        <div class="grid lg:grid-cols-[.85fr_1.15fr] gap-12">
            <div>
                <h2 class="font-headline-md text-headline-md text-on-surface">Find us</h2>
                <div class="mt-6 space-y-5 text-body-sm">
                    <p class="flex gap-3"><span class="material-symbols-outlined text-primary !text-[21px]">location_on</span><span>Plot 17051, Kgosing Ward<br/>Mogoditshane, Botswana</span></p>
                    <p class="flex gap-3"><span class="material-symbols-outlined text-primary !text-[21px]">call</span><span>
                        <a class="hover:text-primary font-semibold" href="https://wa.me/26773674494">+267 73 674 494</a><br/>
                        <a class="hover:text-primary font-semibold" href="https://wa.me/26772661691">+267 72 661 691</a><br/>
                        <span class="text-outline">Call or WhatsApp</span></span></p>
                    <p class="flex gap-3"><span class="material-symbols-outlined text-primary !text-[21px]">mail</span><a class="hover:text-primary" href="mailto:bigdreamslilies@gmail.com">bigdreamslilies@gmail.com</a></p>
                    <p class="flex gap-3"><span class="material-symbols-outlined text-primary !text-[21px]">share</span><span>Facebook &amp; TikTok: Little Lillies</span></p>
                    <p class="flex gap-3 gate"><span class="material-symbols-outlined text-secondary !text-[21px]">schedule</span><span>Opening hours to be confirmed</span></p>
                </div>
                <a href="https://www.google.com/maps/search/?api=1&amp;query=Plot+17051+Kgosing+Ward+Mogoditshane+Botswana"
                   class="mt-8 inline-flex items-center gap-2 border-2 border-secondary text-secondary px-6 py-3 rounded-lg font-semibold hover:bg-secondary/5 transition-colors">
                    <span class="material-symbols-outlined !text-[20px]">map</span> Open in Google Maps
                </a>
            </div>

            <form id="enquiry-form" class="feature-card bg-white rounded p-7 md:p-9 space-y-5" novalidate>
                <h2 class="font-headline-md text-headline-md text-on-surface">Send an enquiry</h2>
                <div class="grid sm:grid-cols-2 gap-5">
                    <label class="block"><span class="font-label-bold text-label-bold text-outline uppercase tracking-wider">Your name</span>
                        <input name="parent_name" type="text" required class="mt-2 w-full rounded-lg border-outline-variant-strong bg-white focus:border-primary focus:ring-primary text-body-sm py-3"/></label>
                    <label class="block"><span class="font-label-bold text-label-bold text-outline uppercase tracking-wider">Mobile number</span>
                        <input name="parent_phone" type="tel" required class="mt-2 w-full rounded-lg border-outline-variant-strong bg-white focus:border-primary focus:ring-primary text-body-sm py-3"/></label>
                    <label class="block"><span class="font-label-bold text-label-bold text-outline uppercase tracking-wider">Child's age</span>
                        <input name="child_age" type="text" class="mt-2 w-full rounded-lg border-outline-variant-strong bg-white focus:border-primary focus:ring-primary text-body-sm py-3"/></label>
                    <label class="block"><span class="font-label-bold text-label-bold text-outline uppercase tracking-wider">Your area</span>
                        <input name="area" type="text" class="mt-2 w-full rounded-lg border-outline-variant-strong bg-white focus:border-primary focus:ring-primary text-body-sm py-3"/></label>
                </div>
                <label class="block"><span class="font-label-bold text-label-bold text-outline uppercase tracking-wider">Anything you would like to ask</span>
                    <textarea name="message" rows="4" class="mt-2 w-full rounded-lg border-outline-variant-strong bg-white focus:border-primary focus:ring-primary text-body-sm"></textarea></label>
                <label class="flex gap-3 items-start font-body-md text-sm text-on-surface-variant">
                    <input name="consent" type="checkbox" required class="mt-1 rounded border-outline-variant-strong text-primary focus:ring-primary"/>
                    <span>Little Lilies may contact me about my enquiry.</span>
                </label>
                <button type="submit" class="w-full bg-primary-container text-on-primary-container py-4 rounded-full font-label-bold text-label-bold hover:scale-105 transition-colors">Send enquiry</button>
                <p id="enquiry-status" class="text-body-sm text-center" role="status" aria-live="polite"></p>
            </form>
        </div>""")
    ),
)

# ------------------------------------------------------- LEGAL AND 404 ----
def legal(title, intro, blocks):
    inner = "\n".join(
        f"""            <div class="py-6"><h2 class="font-headline-md text-xl font-bold text-on-surface">{h}</h2>
                <p class="mt-2 font-body-md text-sm text-on-surface-variant max-w-2xl">{b}</p></div>"""
        for h, b in blocks)
    return section(f"""        <p class="font-body-lg text-body-lg text-on-surface-variant max-w-2xl">{intro}</p>
        <div class="mt-8 divide-y divide-outline-variant max-w-[70ch]">
{inner}
        </div>""")

PAGES["privacy.html"] = dict(
    title="Privacy | Little Lilies Pre-School",
    desc="How Little Lilies Pre-School collects, uses and protects the information you give us.",
    hero=("Privacy", "How we handle your information",
          "We ask for as little as we need, and we do not share it."),
    body=legal("Privacy", "This page explains what we collect through this website and what we do with it.", [
        ("What we collect", "When you send an enquiry we collect your name, mobile number, your child's age, your area and anything you write in the message, together with your consent to reply to you."),
        ("Why we collect it", "So that a member of staff can answer your enquiry, arrange a visit and follow up with you. We do not use it for anything else."),
        ("Who can see it", "Staff at Little Lilies who handle admissions. We do not sell it, and we do not share it with anyone outside the school."),
        ("Children's information", "Detailed information about your child is collected on the enrolment and medical forms, not through this website, and is kept confidential to the staff who care for them."),
        ("Photographs", "We do not publish photographs of children without written permission from a parent or guardian, and you can withdraw that permission at any time."),
        ("Getting in touch", "To ask what we hold about you, or to have it removed, email bigdreamslilies@gmail.com or call +267 73 674 494."),
    ]),
)

PAGES["terms.html"] = dict(
    title="Terms | Little Lilies Pre-School",
    desc="Terms of use for the Little Lilies Pre-School website.",
    hero=("Terms", "Using this website",
          "The short version: the information here is offered in good faith, and a place is only confirmed in writing."),
    body=legal("Terms", "These terms cover your use of this website.", [
        ("Information on this site", "We keep fees, ages and details as accurate as we can. Where something is still being confirmed with the school we mark it as such rather than guess."),
        ("Fees", "Fees shown are current at the time of publication and are reviewed periodically. The fee schedule we send you in writing is the one that applies."),
        ("Enrolment", "Sending an enquiry or completing a form does not by itself reserve a place. A place is confirmed once the registration fee has been received and we have confirmed it to you in writing."),
        ("Downloads", "The forms and documents on this site are provided for you to read and complete. Please use the current version from this site rather than an older copy."),
        ("Links", "Where we link to other services, such as WhatsApp or Google Maps, those services have their own terms."),
        ("Contact", "Questions about these terms: bigdreamslilies@gmail.com."),
    ]),
)

PAGES["404.html"] = dict(
    title="Page not found | Little Lilies Pre-School",
    desc="That page could not be found. Find your way back to Little Lilies Pre-School.",
    hero=("404", "We could not find that page",
          "It may have moved, or the address may have a typo in it. Here is the way back."),
    body=section("""        <div class="text-center">
            <a href="index.html" class="inline-flex items-center bg-primary-container text-on-primary-container py-4 px-8 rounded-full font-label-bold text-label-bold hover:scale-105 transition-colors">Back to the homepage</a>
            <p class="mt-8 font-body-md text-sm text-on-surface-variant">Or try <a class="text-primary font-semibold hover:underline" href="admissions.html">Admissions &amp; fees</a>, <a class="text-primary font-semibold hover:underline" href="faq.html">the questions parents ask</a>, or <a class="text-primary font-semibold hover:underline" href="contact.html">contact us</a>.</p>
        </div>"""),
)


def build():
    for page, spec in PAGES.items():
        eyebrow, title, lede = spec["hero"]
        html = (head(page, spec["title"], spec["desc"])
                + header(page)
                + page_hero(eyebrow, title, lede)
                + spec["body"]
                + footer())
        (ROOT / page).write_text(html)
        print(f"  {page:20s} {len(html):>7,} bytes")
    print(f"\n{len(PAGES)} pages built.")


if __name__ == "__main__":
    build()
