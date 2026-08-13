---
name: Radiant Hearts
colors:
  surface: '#f7f9ff'
  surface-dim: '#ccdced'
  surface-bright: '#f7f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#ecf4ff'
  surface-container: '#e1efff'
  surface-container-high: '#daeafb'
  surface-container-highest: '#d4e4f5'
  on-surface: '#0d1d29'
  on-surface-variant: '#43474e'
  inverse-surface: '#23323f'
  inverse-on-surface: '#e7f2ff'
  outline: '#73777f'
  outline-variant: '#c3c6cf'
  surface-tint: '#406089'
  primary: '#001a35'
  on-primary: '#ffffff'
  primary-container: '#062f55'
  on-primary-container: '#7898c3'
  inverse-primary: '#a9c9f7'
  secondary: '#974800'
  on-secondary: '#ffffff'
  secondary-container: '#fd8a32'
  on-secondary-container: '#652e00'
  tertiary: '#1d1913'
  on-tertiary: '#ffffff'
  tertiary-container: '#322e27'
  on-tertiary-container: '#9c958c'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d3e4ff'
  primary-fixed-dim: '#a9c9f7'
  on-primary-fixed: '#001c38'
  on-primary-fixed-variant: '#27486f'
  secondary-fixed: '#ffdbc7'
  secondary-fixed-dim: '#ffb688'
  on-secondary-fixed: '#311300'
  on-secondary-fixed-variant: '#733600'
  tertiary-fixed: '#eae1d6'
  tertiary-fixed-dim: '#cdc5bb'
  on-tertiary-fixed: '#1f1b15'
  on-tertiary-fixed-variant: '#4b463e'
  background: '#f7f9ff'
  on-background: '#0d1d29'
  surface-variant: '#d4e4f5'
typography:
  display:
    fontFamily: Poppins
    fontSize: 56px
    fontWeight: '600'
    lineHeight: 60px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Poppins
    fontSize: 40px
    fontWeight: '600'
    lineHeight: 46px
    letterSpacing: -0.015em
  headline-md:
    fontFamily: Poppins
    fontSize: 28px
    fontWeight: '600'
    lineHeight: 34px
  headline-sm:
    fontFamily: Poppins
    fontSize: 20px
    fontWeight: '500'
    lineHeight: 28px
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 26px
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 22px
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.22em
  display-mobile:
    fontFamily: Poppins
    fontSize: 36px
    fontWeight: '600'
    lineHeight: 42px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 64px
  container-max: 1200px
---

## Brand & Style

The design system is built for a premium early-learning environment that balances high-institutional trust with the warmth of a home. It draws heavily from Montessori principles—cleanliness, order, and beauty—implemented through a Scandinavian aesthetic.

The visual narrative is "Warm to the child, Precise to the parent." It uses high-quality whitespace to create a sense of calm and focus, avoiding the cluttered, "primary-color-chaos" typical of the sector. The style is **Corporate / Modern** with **Minimalist** layout influences, ensuring every element has a purpose and room to breathe.

- **Tone:** Professional, nurturing, sophisticated, and optimistic.
- **Target Audience:** Modern parents seeking an intentional, high-standard educational foundation for their children.
- **Visual Goal:** To evoke a feeling of "Serious about learning, warm about children."

## Colors

The palette uses **Heart Navy** as the voice of the institution, providing stability and authority. **Playful Orange** is the secondary accent, used for highlights and calls to action to bring joy and energy.

**Color Usage Guidelines:**
- **Heart Navy (#062F55):** Headlines, body text, dark panels, and primary buttons.
- **Playful Orange (#E97B23):** Icon accents, active states, and age-group tags. *Never use for body text.*
- **Soft Cream (#FDF4E9):** Default tinted background for panels and containers to add warmth.
- **Pure White (#FFFFFF):** The primary page background and card surface color.
- **Deep Amber (#B35A12):** Use this for orange text on white backgrounds to ensure AA accessibility.
- **Sky Wash (#EAF1F6):** A secondary light background used for subtle differentiation of sections.

## Typography

The typography system relies on the geometric clarity of **Poppins** for hierarchy and the technical precision of **Inter** for readability.

- **Left-align everything:** Center-alignment is reserved only for logos and short signage lines.
- **Measure:** Keep body text between 45–70 characters per line to prevent fatigue.
- **Rhythm:** Vertical spacing follows an 8px scale (8, 16, 24, 32, 48, 64).
- **Numbers:** Use Poppins 600 for important stats, ratios, and fees to make them scannable.
- **Hierarchy Limitation:** Never use more than three type sizes in a single block.

## Layout & Spacing

This design system uses a **12-column fluid grid** for desktop and a **4-column grid** for mobile. The layout is defined by generous outer margins and a clear 8px spacing rhythm.

- **Grid:** 12 columns with 24px gutters.
- **Margins:** 64px on desktop to create a premium, uncrowded feel.
- **Content Blocks:** Use "The Arc" or "The Block" graphic elements as section dividers or to frame content.
- **Rhythm:** All vertical gaps between components must be multiples of 8px.

## Elevation & Depth

To maintain the clean Scandinavian aesthetic, depth is created through **Tonal Layers** and **Soft Shadows**. 

- **Surface Strategy:** Cards sit on Soft Cream (#FDF4E9) or White (#FFFFFF) surfaces.
- **Shadows:** Use a "soft 8%" shadow (e.g., `0px 4px 20px rgba(6, 47, 85, 0.08)`). The shadow color should be a tint of Heart Navy to ensure it feels integrated rather than grey/muddy.
- **Dividers:** Use 1px Navy hairlines for subtle separation. Avoid heavy borders or high-contrast shadows.

## Shapes

The shape language is defined by high-radius curves, reflecting the "Heart" and "Tree" arcs of the brand identity.

- **Standard Radius:** 0.5rem (8px) for small elements like tags or inputs.
- **Card Radius (Large):** 1.5rem (24px) for all primary containers and images.
- **Graphic Elements:** "The Arc" uses a single large-radius corner (often 100px+) to create a proprietary framing device for the system.
- **Icons:** Fully rounded caps and joins on a 48x48 grid with a 3.2px stroke.

## Components

### Buttons
- **Primary:** Solid Heart Navy with White text. Fully rounded (pill) or 12px radius.
- **Secondary (CTA):** Solid Playful Orange with Heart Navy text (16px+ bold).
- **Ghost:** Heart Navy outline (1.5px) with Heart Navy text.

### Cards
- White background, 24px corner radius, soft 8% Navy shadow.
- Inner padding should be generous (typically 32px or 48px).
- Optional: Top-right corner "Arc" treatment in Soft Cream.

### Input Fields
- White background, 1px Navy outline (20% opacity), 8px radius.
- Labels in Graphite, 14px Inter Medium.

### Chips & Tags
- Used for age groups (e.g., "3-4 Years") or status.
- Soft Cream background with Heart Navy text or Sky Wash with Heart Navy text.

### Icons
- Always stroke-based, never filled (except for specific brand marks).
- Minimum size 24px; for smaller sizes, use simple geometric circles.
- One icon per label, always paired with a word beneath it.