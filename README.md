# Radiant Hearts Pre-school Website Project

A premium, modern early-learning website designed for **Radiant Hearts Pre-school**. Built based on high-fidelity designs with a clean Scandinavian aesthetic ("Warm to the child, Precise to the parent").

## Project Structure

This is a multi-page web application using Vite for local development.

```
Radiant Hearts Pre-school/
├── index.html        # Home page (Hero, welcome, programs, rhythm, curriculum FAQ, CTAs)
├── about.html        # About Us page (History, mission, features, testimonials)
├── gallery.html      # Gallery page (Categorized photos of school activities & spaces)
├── news.html         # News & Blog page (Announcements, events, school activities)
├── contact.html      # Contact & Admission form page (Location, contact info, interactive form)
├── main.js           # Central JavaScript (mobile navigation menu, scroll reveals, FAQ accordion)
├── DESIGN.md         # Design system tokens and styling guidelines
├── package.json      # Vite build & dev server commands
└── screenshots/      # Design mockups/screenshots for reference
```

## Styling & Design System

The project uses the **Tailwind CSS CDN** with custom configuration matching the school's branding:
- **Primary Color (Heart Navy):** `#062F55` (Stability and trust)
- **Secondary Accent (Playful Orange):** `#E97B23` (Joy and energy)
- **Background Tones:** Soft Cream (`#FDF4E9`), Pure White (`#FFFFFF`), Sky Wash (`#EAF1F6`)
- **Typography:** geometric clarity of **Poppins** for titles/headers, and technical precision of **Inter** for body text.

All guidelines, spacing rhythms (8px grid), shapes, and component rules are documented in [DESIGN.md](DESIGN.md).

## Local Development Quickstart

1. **Install Dependencies:**
   Ensure you have Node.js installed, then run:
   ```bash
   npm install
   ```

2. **Start Local Development Server:**
   Launch the Vite local dev server with hot-module reloading:
   ```bash
   npm run dev
   ```
   This will spin up a local development server (typically at `http://localhost:5173`) and automatically open it in your browser.

3. **Production Build:**
   Compile and optimize the static pages for hosting deployment:
   ```bash
   npm run build
   ```
   The compiled assets will be written to the `dist/` directory.

4. **Preview Production Build:**
   Run a local server to preview the built code:
   ```bash
   npm run preview
   ```

---
*Created and maintained by TapxMedia.*
