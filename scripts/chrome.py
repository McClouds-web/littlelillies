"""Shared page chrome for the Little Lilies site.

Ported from the Stitch "Vibrant Scholastic" export, the nav, footer, blob
utilities and decorative accents follow that code.html directly. Edit here and
re-run build-pages.py; never hand-edit chrome inside a page.

    /* ── Motion ──────────────────────────────────────────────────────
       Builds on .reveal above. Grid children come in one after another
       rather than the whole block at once. */
    .reveal-item { opacity:0; transform:translateY(16px);
      transition:opacity .5s var(--ease-out), transform .5s var(--ease-out);
      transition-delay:calc(var(--i, 0) * 70ms); will-change:opacity, transform; }
    .reveal-item.is-in { opacity:1; transform:none; }

    /* Hero copy arrives on load, not on scroll */
    @keyframes ll-rise { from { opacity:0; transform:translateY(16px); } to { opacity:1; transform:none; } }
    .ll-hero-in > * { opacity:0; animation:ll-rise .62s var(--ease-out) forwards; }
    .ll-hero-in > *:nth-child(1) { animation-delay:.06s; }
    .ll-hero-in > *:nth-child(2) { animation-delay:.16s; }
    .ll-hero-in > *:nth-child(3) { animation-delay:.26s; }
    .ll-hero-in > *:nth-child(4) { animation-delay:.34s; }

    /* Colour cards lift, and their icon leans in */
    .ll-card { transition:transform .26s var(--ease-out), box-shadow .26s var(--ease-out); }
    .ll-card:hover { transform:translateY(-6px); box-shadow:0 18px 40px rgba(0,51,102,.14); }
    .ll-card .material-symbols-outlined { transition:transform .26s var(--ease-out); }
    .ll-card:hover .material-symbols-outlined { transform:scale(1.12) rotate(-6deg); }

    /* Photographs breathe on hover instead of jumping */
    .ll-zoom { overflow:hidden; }
    .ll-zoom img { transition:transform .7s var(--ease-out); }
    .ll-zoom:hover img { transform:scale(1.05); }

    /* Buttons answer the press */
    a[class*="rounded-full"], button[class*="rounded-full"] { transition:transform .16s var(--ease-out), filter .16s var(--ease-out); }
    a[class*="rounded-full"]:active, button[class*="rounded-full"]:active { transform:scale(.97); }

    /* The crayon marks drift, slowly and out of sync */
    @keyframes ll-drift { 0%,100% { transform:translate3d(0,0,0) rotate(0deg); }
                          50% { transform:translate3d(0,-12px,0) rotate(3deg); } }
    .ll-mark { animation:ll-drift 11s ease-in-out infinite; }
    .ll-mark[class*="squiggle"] { animation-duration:9s; animation-delay:-2s; }
    .ll-mark[class*="dots"] { animation-duration:13s; animation-delay:-5s; }
    .ll-mark[class*="star"], .ll-mark[class*="burst"] { animation-duration:7.5s; animation-delay:-1s; }
    .ll-mark[class*="blob"] { animation-duration:17s; animation-delay:-8s; }

    /* Header tightens once the page moves */
    nav { transition:height .26s var(--ease-out), box-shadow .26s var(--ease-out); }
    nav.ll-stuck { height:64px !important; }
    nav.ll-stuck img { transform:scale(.9); transition:transform .26s var(--ease-out); }

    /* Accordions open without snapping */
    details summary .material-symbols-outlined { transition:transform .28s var(--ease-out); }
    details[open] > *:not(summary) { animation:ll-rise .34s var(--ease-out) both; }

    /* Links in running text underline as you approach them */
    main a:not([class*="rounded-full"]):not(.dl) { transition:color .2s var(--ease-out); }


    /* ── Touch targets ───────────────────────────────────────────────
       Contact details and accordion headers stay finger-sized on any
       touch screen. Desktop pointers are left alone. */
    summary { min-height:44px; }
    @media (pointer:coarse) {
      a[href^="tel:"], a[href^="mailto:"], a[href*="wa.me"], a[href*="maps.google"], a[href*="google.com/maps"] {
        display:inline-flex; align-items:center; min-height:44px;
      }
      summary { min-height:48px; }
    }

    @media (prefers-reduced-motion:reduce) {
      .reveal-item { opacity:1 !important; transform:none !important; transition:none !important; }
      .ll-hero-in > * { opacity:1 !important; animation:none !important; }
      .ll-mark { animation:none !important; }
      .ll-card:hover, .ll-zoom:hover img { transform:none !important; }
    }
"""

DOMAIN = "https://www.littlelilies.co.bw/"

NAV = [
    ("index.html",      "Home"),
    ("about.html",      "About"),
    ("programs.html",   "Programmes"),
    ("admissions.html", "Admissions"),
    ("gallery.html",    "Gallery"),
    ("faq.html",        "FAQ"),
    ("contact.html",    "Contact"),
]

# The two organic blobs from the export, inlined as data URIs.
STYLE = """
    body { font-family:'Be Vietnam Pro',system-ui,sans-serif; background:#ffffff; color:#1c1c19; }
    h1,h2,h3,h4 { font-family:'Quicksand',sans-serif; }
    .material-symbols-outlined { vertical-align:middle; }

    .bg-blob-primary {
        background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill='%23ffcc33' d='M44.7,-76.4C58.8,-69.2,71.8,-59.1,79.6,-45.8C87.4,-32.6,90,-16.3,87.7,-1.3C85.4,13.7,78.2,27.4,69.5,39.6C60.8,51.8,50.7,62.5,38.1,70.5C25.5,78.5,10.4,83.8,-3.8,89.3C-18,94.8,-31.2,100.5,-42.6,96.6C-54,92.7,-63.5,79.2,-71.5,65.3C-79.5,51.4,-86,37.1,-89,21.8C-92,6.5,-91.5,-9.8,-86.3,-24.1C-81.1,-38.4,-71.2,-50.7,-58.9,-59.6C-46.6,-68.5,-32,-74,-17.7,-74.6C-3.4,-75.2,10.6,-70.9,24.1,-67.2C37.6,-63.5,50.6,-60.5,44.7,-76.4Z' transform='translate(100 100)' /%3E%3C/svg%3E");
        background-repeat:no-repeat; background-size:cover; background-position:center;
    }
    .bg-blob-secondary {
        background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill='%23a4e558' d='M46.7,-73.4C60.8,-66.2,73.8,-56.1,81.6,-42.8C89.4,-29.6,94,-14.8,91.7,0.2C89.4,15.2,80.2,28.9,71.5,41.1C62.8,53.3,54.7,64,42.1,72C29.5,80,14.4,85.3,0.2,85.1C-14,84.9,-28.2,79.2,-39.6,71.3C-51,63.4,-59.5,53.2,-67.5,41.3C-75.5,29.4,-83,15.8,-84,-0.4C-85,-16.6,-79.5,-32.8,-70.3,-46.1C-61.1,-59.4,-48.2,-69.7,-34.9,-75.6C-21.6,-81.5,-7.9,-83.1,5.6,-83.2C19.1,-83.3,32.6,-80.6,46.7,-73.4Z' transform='translate(100 100)' /%3E%3C/svg%3E");
        background-repeat:no-repeat; background-size:cover; background-position:center;
    }

    .feature-card { box-shadow:0 10px 30px rgba(0,51,102,0.03); }
    .feature-card:hover { box-shadow:0 10px 30px rgba(0,51,102,0.08); }

    /* Publishing gate, anything the school has not confirmed in writing. */
    .gate { position:relative; outline:2px dashed #c9873a; outline-offset:8px; border-radius:1rem; }
    .gate::after { content:'UNCONFIRMED'; position:absolute; top:-11px; right:10px;
        font-family:'Be Vietnam Pro',sans-serif; font-size:9px; font-weight:700; letter-spacing:.05em;
        background:#c9873a; color:#fff; padding:2px 8px; border-radius:9999px; }
    @media print { .gate { outline:none; } .gate::after { display:none; } }
"""


def head(page, title, description, extra_style=""):
    canonical = DOMAIN + ("" if page == "index.html" else page)
    return f"""<!DOCTYPE html>
<html class="scroll-smooth" lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>{title}</title>
<meta name="description" content="{description}"/>
<link rel="canonical" href="{canonical}"/>
<link rel="icon" href="favicon.ico" sizes="any"/>
<link rel="icon" type="image/png" sizes="32x32" href="favicon-32.png"/>
<link rel="icon" type="image/png" sizes="16x16" href="favicon-16.png"/>
<link rel="apple-touch-icon" href="apple-touch-icon.png"/>
<meta name="theme-color" content="#ffcc33"/>
<meta name="robots" content="noindex,nofollow"/>
<meta property="og:type" content="website"/>
<meta property="og:url" content="{canonical}"/>
<meta property="og:site_name" content="Little Lilies Pre-School"/>
<meta property="og:title" content="{title}"/>
<meta property="og:description" content="{description}"/>
<link rel="stylesheet" href="assets/tailwind.css"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@500;600;700&amp;family=Be+Vietnam+Pro:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<style>{STYLE}{extra_style}</style>
</head>
<body class="antialiased bg-background">
"""


def header(page):
    desktop, mobile = [], []
    for href, label in NAV:
        on = href == page
        desktop.append(
            f'<a class="{"text-primary font-bold border-b-4 border-primary pb-1" if on else "text-on-surface-variant hover:text-primary transition-colors duration-200"}" href="{href}">{label}</a>')
        mobile.append(
            f'<a class="py-4 {"text-primary font-bold" if on else "text-on-surface-variant"}" href="{href}">{label}</a>')
    return f"""
<nav class="bg-background w-full h-20 sticky top-0 shadow-sm flex justify-between items-center px-gutter max-w-container-max mx-auto z-50 rounded-b-lg">
    <a href="index.html" class="font-headline-md text-headline-md font-bold text-primary flex items-center gap-2 shrink-0">
        <img src="logo/ll-mark.png" alt="" aria-hidden="true" class="h-10 w-auto"/>
        Little Lilies
        <span class="sr-only">Pre-School</span>
    </a>
    <div class="hidden lg:flex items-center gap-8 font-label-bold text-label-bold">
        {chr(10) .join('        ' + d for d in desktop)}
    </div>
    <div class="hidden sm:block">
        <a href="contact.html" class="bg-primary-container text-on-primary-container font-label-bold text-label-bold py-3 px-6 rounded-full hover:brightness-95 transition-all duration-300 shadow-sm inline-flex items-center gap-2">
            Enquire Now

        </a>
    </div>
    <button id="mobile-menu-trigger" class="lg:hidden text-primary p-2" aria-label="Open menu">
        <span class="material-symbols-outlined text-3xl">menu</span>
    </button>
</nav>

<div id="mobile-menu" class="fixed inset-y-0 right-0 z-50 w-full max-w-sm bg-surface-container-lowest transform translate-x-full transition-transform duration-300 ease-in-out lg:hidden shadow-xl">
    <div class="flex flex-col h-full p-6">
        <div class="flex justify-between items-center mb-8">
            <span class="font-headline-md text-xl font-bold text-primary flex items-center gap-2">
                <img src="logo/ll-mark.png" alt="" aria-hidden="true" class="h-9 w-auto"/> Little Lilies
            </span>
            <button id="mobile-menu-close" class="text-primary p-2" aria-label="Close menu">
                <span class="material-symbols-outlined text-2xl">close</span>
            </button>
        </div>
        <div class="flex flex-col divide-y divide-outline-variant font-label-bold text-base mb-auto">
        {chr(10) .join('        ' + m for m in mobile)}
        </div>
        <a href="contact.html" class="block w-full bg-primary-container text-on-primary-container text-center py-4 rounded-full font-label-bold text-label-bold">Enquire Now</a>
    </div>
</div>
"""


def page_hero(eyebrow, title, lede):
    return f"""
<main>
<section class="relative pt-8 pb-12 px-gutter max-w-container-max mx-auto overflow-hidden">
    <div class="absolute top-0 -left-20 w-96 h-96 bg-blob-primary opacity-20 -z-10 animate-spin-slow" aria-hidden="true"></div>
    <div class="absolute -bottom-24 -right-20 w-[30rem] h-[30rem] bg-blob-secondary opacity-20 -z-10" aria-hidden="true"></div>
    <div class="relative z-10 text-center max-w-3xl mx-auto py-8">
        <div class="inline-flex items-center gap-2 px-4 py-2 bg-surface-container rounded-full text-primary font-label-bold text-label-bold">
            <span class="material-symbols-outlined text-sm" style="font-variation-settings:'FILL' 1;">star</span>
            {eyebrow}
        </div>
        <h1 class="mt-6 font-display-lg text-headline-lg-mobile md:text-display-lg text-on-surface">{title}</h1>
        <p class="mt-6 font-body-lg text-body-lg text-on-surface-variant">{lede}</p>
    </div>
</section>
"""


CTA_BAND = """
<section class="px-gutter my-12">
    <div class="max-w-container-max mx-auto bg-secondary rounded-xl px-8 md:px-16 py-section-padding-mobile text-center relative overflow-hidden">
        <div class="absolute -top-16 -right-16 w-72 h-72 bg-blob-primary opacity-20" aria-hidden="true"></div>
        <h2 class="relative font-headline-lg text-headline-lg-mobile md:text-headline-lg text-white">Ready to Get Started?</h2>
        <p class="relative mt-4 font-body-lg text-body-lg text-white/85 max-w-xl mx-auto">
            Come and see the rooms, meet the teachers, and watch what actually happens in a day.
        </p>
        <div class="relative mt-8 flex flex-wrap justify-center gap-4">
            <a href="contact.html" class="bg-primary-container text-on-primary-container font-label-bold text-label-bold py-4 px-8 rounded-full shadow-lg hover:scale-105 transition-transform duration-300 inline-flex items-center gap-2">
                Book a Visit <span class="material-symbols-outlined text-base">arrow_forward</span>
            </a>
            <a href="https://wa.me/26773674494" class="bg-transparent border-2 border-white/60 text-white font-label-bold text-label-bold py-4 px-8 rounded-full hover:bg-white/10 transition-colors duration-300 inline-flex items-center gap-2">
                <span class="material-symbols-outlined text-base">chat</span> WhatsApp
            </a>
        </div>
    </div>
</section>
"""


def footer():
    col1 = "\n".join(
        f'                <a class="text-on-surface-variant hover:text-primary transition-colors opacity-80 hover:opacity-100" href="{h}">{l}</a>'
        for h, l in NAV[1:5])
    col2 = "\n".join(
        f'                <a class="text-on-surface-variant hover:text-primary transition-colors opacity-80 hover:opacity-100" href="{h}">{l}</a>'
        for h, l in NAV[5:])
    return f"""
</main>

<footer class="bg-surface-container w-full rounded-t-lg mt-12 py-section-padding-mobile md:py-section-padding-desktop px-gutter">
    <div class="max-w-container-max mx-auto grid grid-cols-1 md:grid-cols-3 gap-gutter">
        <div class="space-y-4">
            <div class="font-headline-md text-headline-md font-bold text-primary flex items-center gap-2">
                <img src="logo/ll-mark.png" alt="" aria-hidden="true" class="h-9 w-auto"/>
                Little Lilies
            </div>
            <p class="font-body-md text-body-md text-on-surface-variant max-w-xs">
                Little steps, big dreams. Structured early learning and daily English in Mogoditshane.
            </p>
            <p class="font-body-md text-sm text-on-surface-variant">
                Plot 17051, Kgosing Ward, Mogoditshane<br/>
                <a class="hover:text-primary" href="https://wa.me/26773674494">+267 73 674 494</a> &middot;
                <a class="hover:text-primary" href="https://wa.me/26772661691">+267 72 661 691</a><br/>
                <a class="hover:text-primary" href="tel:+2673961190">+267 39 61 190</a><br/>
                <a class="hover:text-primary" href="mailto:bigdreamslilies@gmail.com">bigdreamslilies@gmail.com</a><br/>
                www.littlelilies.co.bw
            </p>
        </div>
        <div class="md:col-span-2 grid grid-cols-2 md:grid-cols-3 gap-8">
            <div class="flex flex-col gap-3 font-label-bold text-label-bold">
{col1}
            </div>
            <div class="flex flex-col gap-3 font-label-bold text-label-bold">
{col2}
                <a class="text-on-surface-variant hover:text-primary transition-colors opacity-80 hover:opacity-100" href="admissions.html#downloads">Downloads</a>
            </div>
            <div class="flex flex-col gap-3 font-label-bold text-label-bold">
                <a class="text-on-surface-variant hover:text-primary transition-colors opacity-80 hover:opacity-100" href="privacy.html">Privacy Policy</a>
                <a class="text-on-surface-variant hover:text-primary transition-colors opacity-80 hover:opacity-100" href="terms.html">Terms of Service</a>
            </div>
        </div>
    </div>
    <div class="max-w-container-max mx-auto mt-10 pt-6 border-t border-outline-variant font-body-md text-sm text-on-surface-variant">
        &copy; 2026 Little Lilies Pre-School. Nurturing growth with every bloom.
    </div>
</footer>

<script type="module" src="main.js"></script>
</body>
</html>
"""
