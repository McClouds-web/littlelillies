document.addEventListener('DOMContentLoaded', () => {
    // Mobile Menu Toggle
    const mobileMenuTrigger = document.getElementById('mobile-menu-trigger');
    const mobileMenu = document.getElementById('mobile-menu');
    const mobileMenuClose = document.getElementById('mobile-menu-close');

    if (mobileMenuTrigger && mobileMenu) {
        mobileMenuTrigger.addEventListener('click', () => {
            mobileMenu.classList.remove('translate-x-full');
        });
    }

    if (mobileMenuClose && mobileMenu) {
        mobileMenuClose.addEventListener('click', () => {
            mobileMenu.classList.add('translate-x-full');
        });
    }

    // Close menu when clicking on a link
    if (mobileMenu) {
        const mobileLinks = mobileMenu.querySelectorAll('a');
        mobileLinks.forEach(link => {
            link.addEventListener('click', () => {
                mobileMenu.classList.add('translate-x-full');
            });
        });
    }

    // Page Scroll Effect for Header Navigation Bar
    const header = document.querySelector('nav');
    if (header) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 10) {
                header.classList.add('shadow-md', 'bg-surface/95');
                header.classList.remove('bg-surface/90');
            } else {
                header.classList.remove('shadow-md', 'bg-surface/95');
                header.classList.add('bg-surface/90');
            }
        });
    }

    // Reveal on scroll. Deliberately short and without a slide: the page is
    // editorial rather than animated, and a long translate reads as decoration.
    // Anything hidden here is only ever hidden after JS has confirmed it can
    // reveal it again, so content still renders with scripting off.
    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (!reduceMotion && 'IntersectionObserver' in window) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (!entry.isIntersecting) return;
                entry.target.classList.remove('opacity-0');
                observer.unobserve(entry.target);
            });
        }, { threshold: 0.08, rootMargin: '0px 0px -40px 0px' });

        document.querySelectorAll('main section > div').forEach(el => {
            if (el.closest('nav') || el.classList.contains('no-anim') || el.closest('#mobile-menu')) return;
            el.classList.add('transition-opacity', 'duration-500', 'opacity-0');
            observer.observe(el);
        });
    }

    // Accordion toggle for FAQ (if present on page)
    const accordions = document.querySelectorAll('.group.cursor-pointer');
    accordions.forEach(acc => {
        acc.addEventListener('click', () => {
            const content = acc.querySelector('div:last-child');
            // chevron icons were removed sitewide, so the icon is optional here
            const icon = acc.querySelector('.material-symbols-outlined');
            if (content) {
                const opening = content.classList.contains('hidden');
                content.classList.toggle('hidden', !opening);
                if (icon) icon.style.transform = opening ? 'rotate(180deg)' : 'rotate(0deg)';
            }
        });
    });

    // ---- Gallery category filter ----
    const filterButtons = document.querySelectorAll('[data-filter]');
    const galleryItems = document.querySelectorAll('.masonry-item[data-cat]');
    if (filterButtons.length && galleryItems.length) {
        const ACTIVE = ['bg-primary', 'text-on-primary'];
        const IDLE = ['bg-surface-container', 'text-primary'];

        const setActive = (btn) => {
            filterButtons.forEach(b => {
                const on = b === btn;
                b.classList.toggle('bg-primary', on);
                b.classList.toggle('text-on-primary', on);
                b.setAttribute('aria-pressed', on ? 'true' : 'false');
            });
        };

        filterButtons.forEach(btn => {
            btn.setAttribute('aria-pressed', 'false');
            btn.addEventListener('click', () => {
                const want = btn.dataset.filter;
                galleryItems.forEach(item => {
                    const show = want === 'all' || item.dataset.cat === want;
                    item.style.display = show ? '' : 'none';
                });
                setActive(btn);
            });
        });
        // default state
        const initial = document.querySelector('[data-filter="all"]');
        if (initial) setActive(initial);
    }

    const SCHOOL_EMAIL = 'bigdreamslilies@gmail.com';
    // The WhatsApp Business line. Every WhatsApp link on the site points here;
    // the other mobile and the landline are call-only.
    const SCHOOL_WHATSAPP = '26772661691';
    const SCHOOL_PHONE = '+267 72 661 691';

    const flash = (form, message, tone) => {
        let note = form.querySelector('.form-note');
        if (!note) {
            note = document.createElement('p');
            note.className = 'form-note text-body-sm font-body-sm mt-3';
            note.setAttribute('role', 'status');
            note.setAttribute('aria-live', 'polite');
            form.appendChild(note);
        }
        note.textContent = message;
        // Amber for "we need something from you", navy for "this worked".
        note.style.color = tone === 'ok' ? '#0F5132' : '#B35A12';
        return note;
    };

    // ---- Enquiry attribution -------------------------------------------------
    // A parent lands on the home page with a campaign tag, browses, and only
    // then opens the contact page. If we read the query string at submit time
    // the campaign is long gone, so the first page of the visit is what gets
    // remembered, for this tab only.
    const ATTRIBUTION_KEY = 'rh_attribution';
    const attribution = (() => {
        try {
            const stored = sessionStorage.getItem(ATTRIBUTION_KEY);
            if (stored) return JSON.parse(stored);
        } catch (_) { /* private mode, or storage disabled — carry on without it */ }

        const params = new URLSearchParams(window.location.search);
        const first = {
            utm_source: params.get('utm_source'),
            utm_medium: params.get('utm_medium'),
            utm_campaign: params.get('utm_campaign'),
            utm_content: params.get('utm_content'),
            utm_term: params.get('utm_term'),
            landing_page: window.location.href.slice(0, 500),
            referrer: (document.referrer || '').slice(0, 500) || null,
        };
        try { sessionStorage.setItem(ATTRIBUTION_KEY, JSON.stringify(first)); } catch (_) { /* ignore */ }
        return first;
    })();

    // ---- Contact page enquiry form ------------------------------------------
    // Posts to the school's admissions system. Both values below are public by
    // design: the endpoint is open to the internet and the site key only tells
    // the server which school this website belongs to. The school is never
    // named by the browser, and the key can be revoked server-side without
    // touching this file.
    // Little Lilies has no admissions endpoint of its own yet: it is meant to be a
    // second Digital Campus tenant, but that platform has no email provider and no
    // site key has been issued. The endpoint and key below belonged to Radiant
    // Hearts, so posting to them would file our parents' details against another
    // school. Left null deliberately — the submit handler hands the enquiry to the
    // parent's mail app instead. Restore both once Little Lilies has its own key.
    const ENQUIRY_ENDPOINT = null;
    const ENQUIRY_SITE_KEY = null;

    // The groups named in the prospectus. "Other Inquiry" is a reason for writing,
    // not a group the school runs, so anything off this list is sent as null.
    // The real group split for two-and-a-half to five years is still unconfirmed
    // by the client; revisit this list once it is.
    const CLASS_NAMES = ['Settling In', 'Language & Play', 'Early Concepts', 'School Ready'];

    const contactForm = document.getElementById('enquiry-form');
    if (contactForm) {
        const button = contactForm.querySelector('[data-submit]');
        const buttonLabel = button ? button.textContent.trim() : 'Send Message';
        let sending = false;

        // WhatsApp is the school's staffed channel, so an enquiry that cannot be
        // posted is handed to WhatsApp rather than to a mail app: a phone with no
        // mail account configured swallows a mailto: and the parent sees nothing
        // happen at all.
        const whatsappFallback = (name, email, phone, topic, message) => {
            const body = [
                'Website enquiry',
                'Name: ' + name,
                'Email: ' + email,
                phone ? 'Phone: ' + phone : null,
                topic ? 'Enquiry about: ' + topic : null,
                '',
                message,
            ].filter(Boolean).join('\n');
            return 'https://wa.me/' + SCHOOL_WHATSAPP + '?text=' + encodeURIComponent(body);
        };

        contactForm.addEventListener('submit', async (e) => {
            e.preventDefault();

            // A second tap on a slow connection must not book a second visit.
            if (sending) return;

            const val = (id) => {
                const el = document.getElementById(id);
                return el ? el.value.trim() : '';
            };
            const name = val('enq-name');
            const email = val('enq-email');
            const phone = val('enq-phone');
            const message = val('enq-message');
            const program = val('enq-program');
            const consent = document.getElementById('consent');

            if (!name || !email || !message) {
                flash(contactForm, 'Please add your name, email and a message.');
                return;
            }
            if (consent && !consent.checked) {
                flash(contactForm, 'Please tick the consent box so we know we may reply to you.');
                consent.focus();
                return;
            }

            // No endpoint yet (see note above), so the enquiry goes out on WhatsApp.
            // Nothing is cleared: if they back out of WhatsApp, everything they
            // typed is still on screen.
            if (!ENQUIRY_ENDPOINT) {
                window.location.href = whatsappFallback(name, email, phone, program, message);
                flash(contactForm, 'Opening WhatsApp so you can send this enquiry to us.', 'ok');
                return;
            }

            sending = true;
            if (button) {
                button.disabled = true;
                button.setAttribute('aria-busy', 'true');
                button.textContent = 'Sending...';
            }
            flash(contactForm, 'Sending your enquiry...');

            let response;
            try {
                response = await fetch(ENQUIRY_ENDPOINT, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        key: ENQUIRY_SITE_KEY,
                        guardian_name: name,
                        guardian_email: email,
                        guardian_phone: phone || null,
                        message: message,
                        class_name: CLASS_NAMES.indexOf(program) === -1 ? null : program,
                        source: 'website',
                        company: (document.getElementById('enq-company') || {}).value || '',
                        utm_source: attribution.utm_source,
                        utm_medium: attribution.utm_medium,
                        utm_campaign: attribution.utm_campaign,
                        utm_content: attribution.utm_content,
                        utm_term: attribution.utm_term,
                        landing_page: attribution.landing_page,
                        referrer: attribution.referrer,
                    }),
                });
            } catch (_) {
                response = null; // offline, DNS failure, blocked request
            }

            const restore = () => {
                sending = false;
                if (button) {
                    button.disabled = false;
                    button.removeAttribute('aria-busy');
                    button.textContent = buttonLabel;
                }
            };

            // Nothing below clears the form. If sending failed, everything the
            // parent typed is still on screen and the retry costs one tap.
            if (!response) {
                restore();
                const note = flash(contactForm, 'We could not reach the school just now. Please check your connection and try again, or ');
                const link = document.createElement('a');
                link.href = whatsappFallback(name, email, phone, program, message);
                link.textContent = 'send this on WhatsApp instead';
                link.className = 'underline';
                note.appendChild(link);
                note.appendChild(document.createTextNode('.'));
                return;
            }

            if (response.status === 429) {
                restore();
                flash(contactForm, 'That is a few enquiries in a short time. Please wait a few minutes and try again, or call us on ' + SCHOOL_PHONE + '.');
                return;
            }

            if (!response.ok) {
                restore();
                const note = flash(contactForm, 'Something went wrong at our end and your enquiry was not sent. Please try again, or ');
                const link = document.createElement('a');
                link.href = whatsappFallback(name, email, phone, program, message);
                link.textContent = 'send this on WhatsApp instead';
                link.className = 'underline';
                note.appendChild(link);
                note.appendChild(document.createTextNode('.'));
                return;
            }

            let reference = null;
            try {
                const payload = await response.json();
                reference = payload && payload.reference;
            } catch (_) { /* a 200 without a body still means it was received */ }

            // Deliberately not restoring the button: the enquiry is in, and
            // re-enabling it invites a duplicate.
            sending = false;
            if (button) {
                button.disabled = true;
                button.removeAttribute('aria-busy');
                button.textContent = 'Enquiry sent';
            }
            contactForm.reset();
            flash(
                contactForm,
                reference
                    ? 'Thank you. Your enquiry is with our admissions team — your reference is ' + reference + '. We will be in touch shortly.'
                    : 'Thank you. Your enquiry is with our admissions team and we will be in touch shortly.',
                'ok',
            );
        });
    }

    // Newsletter forms (footer on every page)
    document.querySelectorAll('form').forEach(form => {
        if (form === contactForm) return;
        const emailField = form.querySelector('input[type="email"]');
        if (!emailField || !form.querySelector('button')) return;
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            const address = emailField.value.trim();
            if (!address) { flash(form, 'Please enter your email address.'); return; }
            window.location.href = 'mailto:' + SCHOOL_EMAIL +
                '?subject=' + encodeURIComponent('Newsletter signup') +
                '&body=' + encodeURIComponent('Please add this address to the Little Lilies newsletter: ' + address);
            flash(form, 'Opening your email app to confirm your signup...');
        });
    });

    // Contact page newsletter arrow -> focus the footer signup field
    const newsletterArrow = document.querySelector('button [data-icon="arrow_forward"]');
    if (newsletterArrow) {
        const btn = newsletterArrow.closest('button');
        btn.setAttribute('type', 'button');
        btn.setAttribute('aria-label', 'Go to newsletter signup');
        btn.addEventListener('click', () => {
            const target = document.querySelector('footer input[type="email"], form input[type="email"]');
            if (target) { target.scrollIntoView({ block: 'center' }); target.focus(); }
        });
    }
});

