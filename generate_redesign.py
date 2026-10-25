# -*- coding: utf-8 -*-
"""
Builder for ATS Malinovka Ultra-Modern Architectural Landing Page.
Designed with Impeccable, Taste-Skill, and Emil Kowalski motion engineering principles.
"""

import os
import re

print("Starting generation of ATS Malinovka landing page...")

def get_head():
    return '''<!DOCTYPE html>
<html lang="ru" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>АТС Малиновка | Архитектурные загородные резиденции в Ленинградской области</title>
    <meta name="description" content="Готовые и строящиеся загородные дома в 4 коттеджных посёлках Ленинградской области под ключ от 90 000 ₽/м². Строим на собственный капитал. Синхронный Trade-In. Льготная ипотека 6%.">
    <link rel="icon" type="image/png" href="assets/logo.png">

    <!-- Google Fonts: Cormorant Garamond, Plus Jakarta Sans, Space Grotesk -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,600&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">

    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        serif: ['"Cormorant Garamond"', 'Georgia', 'serif'],
                        sans: ['"Plus Jakarta Sans"', '-apple-system', 'BlinkMacSystemFont', 'sans-serif'],
                        mono: ['"Space Grotesk"', 'monospace']
                    },
                    colors: {
                        nordic: {
                            950: '#070908',
                            900: '#0B0E0D',
                            850: '#111413',
                            800: '#171B19',
                            700: '#232926',
                            600: '#343C38',
                            500: '#4A5550'
                        },
                        forest: {
                            900: '#0F1E17',
                            800: '#162A20',
                            700: '#1E382B',
                            600: '#2A4C3B',
                            500: '#3B6852'
                        },
                        brass: {
                            500: '#C5A880',
                            400: '#D4B892',
                            300: '#E2CDB0',
                            200: '#F0E3D1',
                            100: '#F9F5EE'
                        },
                        stone: {
                            50: '#FAF8F5',
                            100: '#F3EFE8',
                            200: '#E6E0D4',
                            300: '#D5CDC0',
                            400: '#B8AEA0'
                        }
                    },
                    boxShadow: {
                        'glow-brass': '0 0 40px -10px rgba(197, 168, 128, 0.35)',
                        'glow-emerald': '0 0 50px -10px rgba(42, 76, 59, 0.4)',
                        'elevation-card': '0 20px 40px -15px rgba(0, 0, 0, 0.07)',
                        'elevation-hover': '0 30px 60px -12px rgba(0, 0, 0, 0.15)'
                    }
                }
            }
        }
    </script>

    <style>
        /* Smooth Native Touch & Scroll */
        * {
            -webkit-tap-highlight-color: transparent;
        }

        /* Emil Kowalski Motion Curves & Tactile Micro-Interactions */
        .btn-spring {
            transition: transform 180ms cubic-bezier(0.16, 1, 0.3, 1), box-shadow 180ms ease, background-color 180ms ease;
        }
        .btn-spring:active {
            transform: scale(0.97);
        }

        /* Glassmorphism & Noise Accents */
        .glass-panel {
            background: rgba(255, 255, 255, 0.72);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.85);
        }

        .glass-panel-dark {
            background: rgba(17, 20, 19, 0.82);
            backdrop-filter: blur(24px);
            -webkit-backdrop-filter: blur(24px);
            border: 1px solid rgba(255, 255, 255, 0.08);
        }

        /* Custom Slider Styling */
        input[type="range"] {
            -webkit-appearance: none;
            appearance: none;
            height: 6px;
            background: #E6E0D4;
            border-radius: 9999px;
            outline: none;
            transition: background 200ms ease;
        }
        input[type="range"]::-webkit-slider-thumb {
            -webkit-appearance: none;
            appearance: none;
            width: 24px;
            height: 24px;
            border-radius: 50%;
            background: #162A20;
            border: 3px solid #C5A880;
            cursor: pointer;
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
            transition: transform 150ms cubic-bezier(0.16, 1, 0.3, 1), background-color 150ms ease;
        }
        input[type="range"]::-webkit-slider-thumb:hover {
            transform: scale(1.15);
            background: #0B0E0D;
        }
        input[type="range"]::-webkit-slider-thumb:active {
            transform: scale(1.05);
        }

        /* Accordion Smooth Height Transition via CSS Grid */
        .accordion-content {
            display: grid;
            grid-template-rows: 0fr;
            transition: grid-template-rows 280ms cubic-bezier(0.16, 1, 0.3, 1), opacity 240ms ease;
            opacity: 0;
        }
        .accordion-item.open .accordion-content {
            grid-template-rows: 1fr;
            opacity: 1;
        }
        .accordion-item.open .accordion-icon {
            transform: rotate(45deg);
        }

        /* Dynamic Donut Chart Progress */
        .donut-circle {
            transition: stroke-dasharray 600ms cubic-bezier(0.16, 1, 0.3, 1), stroke-dashoffset 600ms cubic-bezier(0.16, 1, 0.3, 1);
        }

        /* Custom subtle scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
        }
        ::-webkit-scrollbar-track {
            background: #0B0E0D;
        }
        ::-webkit-scrollbar-thumb {
            background: #232926;
            border-radius: 4px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #C5A880;
        }
    </style>
</head>
<body class="bg-stone-50 text-nordic-900 font-sans antialiased selection:bg-brass-500 selection:text-white">
'''

print("Head template defined.")

def get_nav():
    return '''
    <!-- Floating Glass Header -->
    <header class="fixed top-4 inset-x-0 z-50 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="glass-panel-dark rounded-full px-5 py-3 sm:px-6 sm:py-3.5 flex items-center justify-between shadow-2xl border border-white/10 transition-all duration-300">
            <!-- Brand Logo & Atelier Mark -->
            <a href="#" class="flex items-center space-x-3 group">
                <div class="w-10 h-10 rounded-full bg-forest-900/90 border border-brass-500/40 flex items-center justify-center p-2 shadow-inner group-hover:border-brass-400 transition-colors">
                    <svg viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 text-brass-400">
                        <path d="M20 4L4 34H36L20 4Z" stroke="currentColor" stroke-width="1.75" stroke-linejoin="round"/>
                        <path d="M20 12L10 30H30L20 12Z" stroke="currentColor" stroke-width="1.2" stroke-opacity="0.6"/>
                        <line x1="20" y1="4" x2="20" y2="34" stroke="currentColor" stroke-width="1.2" stroke-opacity="0.8"/>
                        <circle cx="20" cy="20" r="2" fill="currentColor"/>
                    </svg>
                </div>
                <div>
                    <div class="flex items-center space-x-2">
                        <span class="font-serif tracking-widest text-lg font-bold text-white uppercase group-hover:text-brass-300 transition-colors">АТС МАЛИНОВКА</span>
                        <span class="hidden sm:inline-block px-1.5 py-0.5 rounded text-[10px] font-mono uppercase bg-forest-700/80 text-brass-300 border border-forest-600/50">с 2009 г.</span>
                    </div>
                    <span class="text-[10px] tracking-[0.2em] text-stone-400 font-mono block uppercase">Архитектурный девелопмент</span>
                </div>
            </a>

            <!-- Center Status Pill (Desktop) -->
            <div class="hidden lg:flex items-center space-x-2 px-3.5 py-1.5 rounded-full bg-nordic-800/80 border border-white/5 text-xs text-stone-300">
                <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
                <span class="font-medium text-stone-200">4 посёлка открыты:</span>
                <span class="text-stone-400 font-mono text-[11px]">Honkaniemi · Sawoda · HYTTE · Юрки</span>
            </div>

            <!-- Navigation Links (Desktop) -->
            <nav class="hidden md:flex items-center space-x-6 text-xs tracking-wider uppercase font-medium text-stone-300">
                <a href="#villages" class="hover:text-brass-300 transition-colors">Посёлки</a>
                <a href="#standards" class="hover:text-brass-300 transition-colors">Преимущества</a>
                <a href="#calculator" class="hover:text-brass-300 transition-colors">Ипотека 6%</a>
                <a href="#faq" class="hover:text-brass-300 transition-colors">FAQ</a>
                <a href="#about" class="hover:text-brass-300 transition-colors">О девелопере</a>
            </nav>

            <!-- Actions: Phone & VIP Pass -->
            <div class="flex items-center space-x-3">
                <a href="tel:+78126042009" class="hidden sm:flex items-center space-x-2 text-stone-200 hover:text-brass-300 text-xs font-mono tracking-wider transition-colors px-2 py-1">
                    <svg class="w-3.5 h-3.5 text-brass-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
                    <span>+7 (812) 604-20-09</span>
                </a>
                <button onclick="openModal('vipModal')" class="btn-spring px-4 py-2 sm:px-5 sm:py-2.5 rounded-full bg-brass-500 hover:bg-brass-400 text-nordic-950 font-semibold text-xs tracking-wider uppercase shadow-glow-brass flex items-center space-x-2">
                    <span class="hidden xs:inline">VIP</span><span>Трансфер</span>
                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
                </button>
            </div>
        </div>
    </header>
    '''

def get_hero():
    return '''
    <!-- Cinematic Full-Bleed Architectural Hero -->
    <section class="relative min-h-screen flex flex-col justify-between pt-28 pb-12 sm:pt-36 sm:pb-16 bg-nordic-950 text-white overflow-hidden">
        <!-- Hero Dynamic Backgrounds (Switched via JS) -->
        <div class="absolute inset-0 z-0">
            <img id="heroBg0" src="assets/honkaniemi-forest.jpg" alt="Honkaniemi Pines" class="hero-bg absolute inset-0 w-full h-full object-cover object-center scale-105 transition-opacity duration-1000 ease-out opacity-100">
            <img id="heroBg1" src="assets/sawoda-facade-new.png" alt="Sawoda Barnhouse" class="hero-bg absolute inset-0 w-full h-full object-cover object-center scale-105 transition-opacity duration-1000 ease-out opacity-0 pointer-events-none">
            <img id="heroBg2" src="assets/hytte-house.jpg" alt="Hytte Nordic Villa" class="hero-bg absolute inset-0 w-full h-full object-cover object-center scale-105 transition-opacity duration-1000 ease-out opacity-0 pointer-events-none">
            <img id="heroBg3" src="assets/yurki-cottage.jpg" alt="Yurki River Estate" class="hero-bg absolute inset-0 w-full h-full object-cover object-center scale-105 transition-opacity duration-1000 ease-out opacity-0 pointer-events-none">
            
            <!-- Architectural Vignette & Gradient Overlays -->
            <div class="absolute inset-0 bg-gradient-to-t from-nordic-950 via-nordic-950/75 to-nordic-950/45"></div>
            <div class="absolute inset-0 bg-radial-vignette opacity-60"></div>
        </div>

        <!-- Ambient Forest Glow -->
        <div class="absolute top-1/4 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px] bg-forest-600/20 rounded-full blur-[140px] pointer-events-none"></div>

        <!-- Main Hero Content -->
        <div class="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full my-auto">
            <div class="max-w-4xl">
                <!-- Location & Heritage Badge -->
                <div class="inline-flex items-center space-x-3 px-4 py-1.5 rounded-full bg-white/10 backdrop-blur-md border border-white/15 text-xs text-brass-300 font-mono tracking-widest uppercase mb-6 sm:mb-8">
                    <span class="w-1.5 h-1.5 rounded-full bg-brass-400"></span>
                    <span id="heroCoordinates">60°18'N 29°52'E · Карельский перешеек</span>
                    <span class="text-white/40">|</span>
                    <span class="text-stone-300">ИЖС в собственности</span>
                </div>

                <!-- Grand Headline -->
                <h1 class="text-4xl sm:text-6xl md:text-7xl lg:text-8xl font-serif font-normal tracking-tight text-white leading-[1.06] mb-6 sm:mb-8">
                    Дома, в которых хочется <span class="italic font-normal text-brass-300">жить поколениями.</span>
                </h1>

                <!-- Subheadline with Key Differentiators -->
                <p class="text-base sm:text-xl text-stone-300 font-light max-w-2xl leading-relaxed mb-8 sm:mb-10">
                    Архитектурные резиденции в 4 клубных посёлках Ленинградской области под ключ от <span class="text-white font-medium">90 000 ₽/м²</span>. Строим на <span class="text-white font-medium underline decoration-brass-400 decoration-1 underline-offset-4">собственный капитал</span> без ожидания банков. Синхронный Trade-In: живите в городской квартире до дня новоселья.
                </p>

                <!-- Action Triggers -->
                <div class="flex flex-col sm:flex-row items-stretch sm:items-center gap-4 mb-12 sm:mb-16">
                    <button onclick="openModal('catalogModal')" class="btn-spring px-8 py-4 rounded-full bg-brass-500 hover:bg-brass-400 text-nordic-950 font-semibold text-sm tracking-wider uppercase shadow-glow-brass flex items-center justify-center space-x-3 group">
                        <span>Скачать генплан и каталог (PDF)</span>
                        <svg class="w-4 h-4 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
                    </button>
                    <a href="#calculator" class="btn-spring px-8 py-4 rounded-full bg-white/10 hover:bg-white/15 text-white backdrop-blur-md border border-white/20 font-medium text-sm tracking-wider uppercase flex items-center justify-center space-x-2">
                        <svg class="w-4 h-4 text-brass-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 7h6m0 10v-3m-3 3h.01M9 17h.01M9 14h.01M12 14h.01M15 11h.01M12 11h.01M9 11h.01M7 21h10a2 2 0 002-2V5a2 2 0 00-2-2H7a2 2 0 00-2 2v14a2 2 0 002 2z"/></svg>
                        <span>Ипотека 6% в ЛО</span>
                    </a>
                    <button onclick="openModal('vipModal')" class="sm:hidden btn-spring px-6 py-3.5 rounded-full bg-forest-700/80 text-brass-300 border border-brass-500/40 text-xs font-semibold uppercase tracking-wider text-center">
                        VIP-трансфер на Mercedes
                    </button>
                </div>

                <!-- Proof Metrics Bar -->
                <div class="grid grid-cols-2 md:grid-cols-4 gap-4 sm:gap-6 pt-6 border-t border-white/15">
                    <div>
                        <div class="text-2xl sm:text-3xl font-serif text-white font-normal">4 посёлка</div>
                        <div class="text-xs text-stone-400 font-mono tracking-wider mt-1">в лучших локациях ЛО</div>
                    </div>
                    <div>
                        <div class="text-2xl sm:text-3xl font-serif text-brass-300 font-normal">от 6.0%</div>
                        <div class="text-xs text-stone-400 font-mono tracking-wider mt-1">Семейная и IT ипотека</div>
                    </div>
                    <div>
                        <div class="text-2xl sm:text-3xl font-serif text-white font-normal">7 дней</div>
                        <div class="text-xs text-stone-400 font-mono tracking-wider mt-1">выход на стройку (свой капитал)</div>
                    </div>
                    <div>
                        <div class="text-2xl sm:text-3xl font-serif text-brass-300 font-normal">Trade-In</div>
                        <div class="text-xs text-stone-400 font-mono tracking-wider mt-1">квартира в зачет дома</div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Interactive Hero Settlement Switcher Bar (Bottom) -->
        <div class="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full mt-6">
            <div class="glass-panel-dark rounded-2xl p-2.5 sm:p-3 border border-white/10 shadow-2xl">
                <div class="text-[11px] font-mono uppercase tracking-widest text-stone-400 mb-2 px-3 flex items-center justify-between">
                    <span>Интерактивный выбор посёлка:</span>
                    <span class="hidden sm:inline text-brass-400">Нажмите на карточку для просмотра атмосферы</span>
                </div>
                <div class="grid grid-cols-2 lg:grid-cols-4 gap-2">
                    <!-- Village 0: Honkaniemi -->
                    <button onclick="switchHeroVillage(0)" id="heroTab0" class="hero-village-tab active text-left p-3 rounded-xl bg-white/15 border border-brass-400/80 transition-all duration-300 group">
                        <div class="flex items-center justify-between mb-1">
                            <span class="font-serif text-sm sm:text-base font-bold text-white group-hover:text-brass-300">Honkaniemi</span>
                            <span class="text-[10px] font-mono text-brass-400">от 14.8 млн</span>
                        </div>
                        <p class="text-[11px] text-stone-300 line-clamp-1">Выборгский р-н · Озера и бор</p>
                    </button>

                    <!-- Village 1: Sawoda -->
                    <button onclick="switchHeroVillage(1)" id="heroTab1" class="hero-village-tab text-left p-3 rounded-xl bg-white/5 border border-white/10 hover:bg-white/10 transition-all duration-300 group">
                        <div class="flex items-center justify-between mb-1">
                            <span class="font-serif text-sm sm:text-base font-bold text-white group-hover:text-brass-300">Sawoda</span>
                            <span class="text-[10px] font-mono text-stone-400 group-hover:text-brass-400">от 9.9 млн</span>
                        </div>
                        <p class="text-[11px] text-stone-400 line-clamp-1">Тосненский р-н · Сканди-Барн</p>
                    </button>

                    <!-- Village 2: HYTTE -->
                    <button onclick="switchHeroVillage(2)" id="heroTab2" class="hero-village-tab text-left p-3 rounded-xl bg-white/5 border border-white/10 hover:bg-white/10 transition-all duration-300 group">
                        <div class="flex items-center justify-between mb-1">
                            <span class="font-serif text-sm sm:text-base font-bold text-white group-hover:text-brass-300">HYTTE</span>
                            <span class="text-[10px] font-mono text-stone-400 group-hover:text-brass-400">от 11.5 млн</span>
                        </div>
                        <p class="text-[11px] text-stone-400 line-clamp-1">Всеволожский р-н · 25 мин до КАД</p>
                    </button>

                    <!-- Village 3: Юрки -->
                    <button onclick="switchHeroVillage(3)" id="heroTab3" class="hero-village-tab text-left p-3 rounded-xl bg-white/5 border border-white/10 hover:bg-white/10 transition-all duration-300 group">
                        <div class="flex items-center justify-between mb-1">
                            <span class="font-serif text-sm sm:text-base font-bold text-white group-hover:text-brass-300">Юрки</span>
                            <span class="text-[10px] font-mono text-stone-400 group-hover:text-brass-400">от 8.9 млн</span>
                        </div>
                        <p class="text-[11px] text-stone-400 line-clamp-1">Кингисеппский р-н · Берег Луги</p>
                    </button>
                </div>
            </div>
        </div>
    </section>
    '''

def get_jtbd():
    return '''
    <!-- JTBD: 3 Architectural Scenarios of Living -->
    <section class="py-24 sm:py-32 bg-stone-100 border-b border-stone-200/80">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <!-- Section Header -->
            <div class="flex flex-col md:flex-row md:items-end justify-between mb-16 sm:mb-20">
                <div class="max-w-2xl">
                    <div class="text-xs font-mono uppercase tracking-widest text-forest-700 font-semibold mb-3">
                        Архитектурные сценарии жизни
                    </div>
                    <h2 class="text-3xl sm:text-5xl font-serif text-nordic-900 tracking-tight leading-tight">
                        Дом, спроектированный под ваш образ жизни, <span class="italic text-forest-600">а не под типовой шаблон.</span>
                    </h2>
                </div>
                <div class="mt-4 md:mt-0 text-sm text-stone-500 font-mono">
                    3 ключевых сценария · ИЖС в собственности
                </div>
            </div>

            <!-- 3 Grid Cards -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <!-- Card 1: Families -->
                <div class="group relative bg-white rounded-3xl p-8 sm:p-10 border border-stone-200/80 shadow-elevation-card hover:shadow-elevation-hover transition-all duration-300 flex flex-col justify-between">
                    <div>
                        <div class="w-12 h-12 rounded-2xl bg-stone-100 border border-stone-200 flex items-center justify-center text-forest-700 mb-6 group-hover:scale-110 group-hover:bg-forest-900 group-hover:text-brass-300 transition-all duration-300">
                            <span class="font-serif text-xl font-bold">01</span>
                        </div>
                        <div class="text-xs font-mono uppercase tracking-wider text-forest-600 font-semibold mb-2">Безопасность и здоровье</div>
                        <h3 class="text-2xl font-serif text-nordic-900 mb-4">Семьям с детьми</h3>
                        <p class="text-sm text-stone-600 leading-relaxed mb-6">
                            Просторные участки от 10 до 25 соток, закрытая охраняемая территория 24/7 с КПП и детскими эко-площадками. Чистейший хвойный воздух Карельского перешейка без городского шума и смога.
                        </p>
                    </div>
                    <ul class="space-y-3 pt-6 border-t border-stone-100 text-xs font-mono text-stone-600">
                        <li class="flex items-center space-x-2">
                            <svg class="w-4 h-4 text-emerald-600 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
                            <span>Семейная ипотека 6% (лимит до 12 млн ₽)</span>
                        </li>
                        <li class="flex items-center space-x-2">
                            <svg class="w-4 h-4 text-emerald-600 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
                            <span>Детские эко-парки и безопасность без машин</span>
                        </li>
                    </ul>
                </div>

                <!-- Card 2: IT & Remote -->
                <div class="group relative bg-white rounded-3xl p-8 sm:p-10 border border-stone-200/80 shadow-elevation-card hover:shadow-elevation-hover transition-all duration-300 flex flex-col justify-between">
                    <div>
                        <div class="w-12 h-12 rounded-2xl bg-stone-100 border border-stone-200 flex items-center justify-center text-forest-700 mb-6 group-hover:scale-110 group-hover:bg-forest-900 group-hover:text-brass-300 transition-all duration-300">
                            <span class="font-serif text-xl font-bold">02</span>
                        </div>
                        <div class="text-xs font-mono uppercase tracking-wider text-forest-600 font-semibold mb-2">Фокус и скорость</div>
                        <h3 class="text-2xl font-serif text-nordic-900 mb-4">Удалёнщикам и IT</h3>
                        <p class="text-sm text-stone-600 leading-relaxed mb-6">
                            Оптоволокно до 500 Мбит/с прямо в дом, тишина соснового леса для глубокого фокуса, панорамные кабинеты с видом на лес и быстрый выезд в Петербург (25–45 минут по ЗСД / М-11).
                        </p>
                    </div>
                    <ul class="space-y-3 pt-6 border-t border-stone-100 text-xs font-mono text-stone-600">
                        <li class="flex items-center space-x-2">
                            <svg class="w-4 h-4 text-emerald-600 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
                            <span>IT-ипотека 6% в ЛО (лимит до 9 млн ₽)</span>
                        </li>
                        <li class="flex items-center space-x-2">
                            <svg class="w-4 h-4 text-emerald-600 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
                            <span>Оптоволокно, резервное питание 15 кВт</span>
                        </li>
                    </ul>
                </div>

                <!-- Card 3: Investors -->
                <div class="group relative bg-white rounded-3xl p-8 sm:p-10 border border-stone-200/80 shadow-elevation-card hover:shadow-elevation-hover transition-all duration-300 flex flex-col justify-between">
                    <div>
                        <div class="w-12 h-12 rounded-2xl bg-stone-100 border border-stone-200 flex items-center justify-center text-forest-700 mb-6 group-hover:scale-110 group-hover:bg-forest-900 group-hover:text-brass-300 transition-all duration-300">
                            <span class="font-serif text-xl font-bold">03</span>
                        </div>
                        <div class="text-xs font-mono uppercase tracking-wider text-forest-600 font-semibold mb-2">Капитализация и аренда</div>
                        <h3 class="text-2xl font-serif text-nordic-900 mb-4">Инвесторам</h3>
                        <p class="text-sm text-stone-600 leading-relaxed mb-6">
                            Земля ИЖС в частной собственности. Рост капитализации объекта на +25–35% от фундамента до чистовой отделки. Высокий круглогодичный спрос на аренду премиальных загородных вилл (от 120 000 ₽/мес).
                        </p>
                    </div>
                    <ul class="space-y-3 pt-6 border-t border-stone-100 text-xs font-mono text-stone-600">
                        <li class="flex items-center space-x-2">
                            <svg class="w-4 h-4 text-emerald-600 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
                            <span>Высокая ликвидность готового объекта</span>
                        </li>
                        <li class="flex items-center space-x-2">
                            <svg class="w-4 h-4 text-emerald-600 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
                            <span>Синхронный Trade-In: зачёт вторички</span>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </section>
    '''

def get_catalog():
    return '''
    <!-- Architectural Catalog of 4 Settlements & Signature Houses -->
    <section id="villages" class="py-24 sm:py-32 bg-stone-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <!-- Header & Filter Tabs -->
            <div class="flex flex-col lg:flex-row lg:items-end justify-between mb-12 sm:mb-16">
                <div>
                    <div class="text-xs font-mono uppercase tracking-widest text-forest-700 font-semibold mb-3">
                        Коллекция 2026 года
                    </div>
                    <h2 class="text-3xl sm:text-5xl font-serif text-nordic-900 tracking-tight leading-tight">
                        4 коттеджных посёлка <span class="italic text-forest-600">и архитектурные проекты.</span>
                    </h2>
                </div>

                <!-- Filter Controls with Sliding Feel -->
                <div class="mt-8 lg:mt-0 flex flex-wrap gap-2 p-1.5 rounded-2xl bg-stone-200/80 border border-stone-300/60 max-w-xl">
                    <button onclick="filterCatalog('all')" class="catalog-filter-btn active px-4 py-2 rounded-xl text-xs font-medium font-mono uppercase tracking-wider bg-forest-900 text-white shadow-sm transition-all duration-200">Все проекты</button>
                    <button onclick="filterCatalog('honkaniemi')" class="catalog-filter-btn px-4 py-2 rounded-xl text-xs font-medium font-mono uppercase tracking-wider text-stone-600 hover:text-nordic-900 transition-all duration-200">Honkaniemi</button>
                    <button onclick="filterCatalog('sawoda')" class="catalog-filter-btn px-4 py-2 rounded-xl text-xs font-medium font-mono uppercase tracking-wider text-stone-600 hover:text-nordic-900 transition-all duration-200">Sawoda</button>
                    <button onclick="filterCatalog('hytte')" class="catalog-filter-btn px-4 py-2 rounded-xl text-xs font-medium font-mono uppercase tracking-wider text-stone-600 hover:text-nordic-900 transition-all duration-200">HYTTE</button>
                    <button onclick="filterCatalog('yurki')" class="catalog-filter-btn px-4 py-2 rounded-xl text-xs font-medium font-mono uppercase tracking-wider text-stone-600 hover:text-nordic-900 transition-all duration-200">Юрки</button>
                    <button onclick="filterCatalog('barn')" class="catalog-filter-btn px-4 py-2 rounded-xl text-xs font-medium font-mono uppercase tracking-wider text-stone-600 hover:text-nordic-900 transition-all duration-200">Scandi Barn</button>
                </div>
            </div>

            <!-- Catalog Cards Grid -->
            <div id="catalogGrid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                <!-- Card 1: Honkaniemi -->
                <div class="catalog-card" data-category="honkaniemi">
                    <div class="bg-white rounded-3xl overflow-hidden border border-stone-200/90 shadow-elevation-card hover:shadow-elevation-hover transition-all duration-300 flex flex-col h-full group">
                        <div class="relative h-72 overflow-hidden bg-nordic-900">
                            <img src="assets/honkaniemi-forest.jpg" alt="Honkaniemi" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 ease-out">
                            <div class="absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-black/20"></div>
                            <div class="absolute top-4 left-4 flex flex-wrap gap-2">
                                <span class="px-3 py-1 rounded-full text-[11px] font-mono uppercase tracking-wider bg-white/90 backdrop-blur-md text-nordic-900 font-semibold">ИЖС</span>
                                <span class="px-3 py-1 rounded-full text-[11px] font-mono uppercase tracking-wider bg-forest-900/90 backdrop-blur-md text-brass-300 border border-brass-500/30">Сосновый бор</span>
                            </div>
                            <div class="absolute bottom-4 left-4 right-4 flex items-end justify-between text-white">
                                <div>
                                    <div class="text-xs font-mono text-stone-300 uppercase">Выборгский район</div>
                                    <h3 class="font-serif text-2xl font-bold">Honkaniemi</h3>
                                </div>
                                <div class="text-right">
                                    <div class="text-xs font-mono text-brass-300">от 14 800 000 ₽</div>
                                    <div class="text-[10px] text-stone-300 font-mono">от 71 200 ₽/мес</div>
                                </div>
                            </div>
                        </div>
                        <div class="p-6 flex-1 flex flex-col justify-between">
                            <div>
                                <p class="text-xs text-stone-600 leading-relaxed mb-4">
                                    Премиальные резиденции на Карельском перешейке в окружении вековых сосен и системы озёр Красногвардейское и Подгорное.
                                </p>
                                <div class="grid grid-cols-2 gap-2 text-xs font-mono text-stone-700 mb-6 bg-stone-50 p-3 rounded-2xl border border-stone-100">
                                    <div><span class="text-stone-400">Площадь:</span> 140–280 м²</div>
                                    <div><span class="text-stone-400">Участки:</span> 12–25 сот.</div>
                                    <div><span class="text-stone-400">Коммуникации:</span> Газ, 15 кВт</div>
                                    <div><span class="text-stone-400">До КАД:</span> 45 минут</div>
                                </div>
                            </div>
                            <div class="flex items-center gap-3 pt-4 border-t border-stone-100">
                                <button onclick="openProjectModal('Honkaniemi', 'Выборгский р-н, пос. Уткино', 'от 14.8 млн ₽', 'assets/honkaniemi-forest.jpg', 'Участки ИЖС от 12 до 25 соток в реликтовом сосновом бору. Первая линия озёр, магистральный газ, 15 кВт, закрытый охраняемый периметр.')" class="btn-spring flex-1 py-3 px-4 rounded-xl bg-forest-900 hover:bg-forest-800 text-white font-mono text-xs uppercase tracking-wider text-center font-semibold">
                                    Генплан и планировка
                                </button>
                                <button onclick="openModal('vipModal')" title="Записаться на просмотр" class="btn-spring p-3 rounded-xl bg-stone-100 hover:bg-stone-200 text-forest-900 border border-stone-200">
                                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
                                </button>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Card 2: Sawoda -->
                <div class="catalog-card" data-category="sawoda">
                    <div class="bg-white rounded-3xl overflow-hidden border border-stone-200/90 shadow-elevation-card hover:shadow-elevation-hover transition-all duration-300 flex flex-col h-full group">
                        <div class="relative h-72 overflow-hidden bg-nordic-900">
                            <img src="assets/sawoda-facade-new.png" alt="Sawoda" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 ease-out">
                            <div class="absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-black/20"></div>
                            <div class="absolute top-4 left-4 flex flex-wrap gap-2">
                                <span class="px-3 py-1 rounded-full text-[11px] font-mono uppercase tracking-wider bg-white/90 backdrop-blur-md text-nordic-900 font-semibold">ИЖС</span>
                                <span class="px-3 py-1 rounded-full text-[11px] font-mono uppercase tracking-wider bg-brass-500/90 backdrop-blur-md text-nordic-950 font-semibold">Магистральный газ</span>
                            </div>
                            <div class="absolute bottom-4 left-4 right-4 flex items-end justify-between text-white">
                                <div>
                                    <div class="text-xs font-mono text-stone-300 uppercase">Тосненский район</div>
                                    <h3 class="font-serif text-2xl font-bold">Sawoda</h3>
                                </div>
                                <div class="text-right">
                                    <div class="text-xs font-mono text-brass-300">от 9 900 000 ₽</div>
                                    <div class="text-[10px] text-stone-300 font-mono">от 47 500 ₽/мес</div>
                                </div>
                            </div>
                        </div>
                        <div class="p-6 flex-1 flex flex-col justify-between">
                            <div>
                                <p class="text-xs text-stone-600 leading-relaxed mb-4">
                                    Клубный скандинавский посёлок в едином архитектурном стиле Barnhouse. Панорамный второй свет, тёплый пол и развитая инфраструктура.
                                </p>
                                <div class="grid grid-cols-2 gap-2 text-xs font-mono text-stone-700 mb-6 bg-stone-50 p-3 rounded-2xl border border-stone-100">
                                    <div><span class="text-stone-400">Площадь:</span> 100–165 м²</div>
                                    <div><span class="text-stone-400">Участки:</span> 8–15 сот.</div>
                                    <div><span class="text-stone-400">Газ:</span> Подключен</div>
                                    <div><span class="text-stone-400">До КАД:</span> 35 минут</div>
                                </div>
                            </div>
                            <div class="flex items-center gap-3 pt-4 border-t border-stone-100">
                                <button onclick="openProjectModal('Sawoda', 'Тосненский район', 'от 9.9 млн ₽', 'assets/sawoda-facade-new.png', 'Скандинавские дома с чистовой отделкой, монолитный фундамент, водяной тёплый пол по всей площади, асфальтированные дороги, магистральный газ.')" class="btn-spring flex-1 py-3 px-4 rounded-xl bg-forest-900 hover:bg-forest-800 text-white font-mono text-xs uppercase tracking-wider text-center font-semibold">
                                    Генплан и планировка
                                </button>
                                <button onclick="openModal('vipModal')" title="Записаться на просмотр" class="btn-spring p-3 rounded-xl bg-stone-100 hover:bg-stone-200 text-forest-900 border border-stone-200">
                                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
                                </button>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Card 3: HYTTE -->
                <div class="catalog-card" data-category="hytte">
                    <div class="bg-white rounded-3xl overflow-hidden border border-stone-200/90 shadow-elevation-card hover:shadow-elevation-hover transition-all duration-300 flex flex-col h-full group">
                        <div class="relative h-72 overflow-hidden bg-nordic-900">
                            <img src="assets/hytte-house.jpg" alt="HYTTE" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 ease-out">
                            <div class="absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-black/20"></div>
                            <div class="absolute top-4 left-4 flex flex-wrap gap-2">
                                <span class="px-3 py-1 rounded-full text-[11px] font-mono uppercase tracking-wider bg-white/90 backdrop-blur-md text-nordic-900 font-semibold">ИЖС</span>
                                <span class="px-3 py-1 rounded-full text-[11px] font-mono uppercase tracking-wider bg-forest-900/90 backdrop-blur-md text-brass-300">25 мин до КАД</span>
                            </div>
                            <div class="absolute bottom-4 left-4 right-4 flex items-end justify-between text-white">
                                <div>
                                    <div class="text-xs font-mono text-stone-300 uppercase">Всеволожский район</div>
                                    <h3 class="font-serif text-2xl font-bold">HYTTE</h3>
                                </div>
                                <div class="text-right">
                                    <div class="text-xs font-mono text-brass-300">от 11 500 000 ₽</div>
                                    <div class="text-[10px] text-stone-300 font-mono">от 55 300 ₽/мес</div>
                                </div>
                            </div>
                        </div>
                        <div class="p-6 flex-1 flex flex-col justify-between">
                            <div>
                                <p class="text-xs text-stone-600 leading-relaxed mb-4">
                                    Концепция нордического уюта Hygge: лаконичный чёрный фасад, просторная терраса из лиственницы, второй свет и лесные деревья на участке.
                                </p>
                                <div class="grid grid-cols-2 gap-2 text-xs font-mono text-stone-700 mb-6 bg-stone-50 p-3 rounded-2xl border border-stone-100">
                                    <div><span class="text-stone-400">Площадь:</span> 110–150 м²</div>
                                    <div><span class="text-stone-400">Участки:</span> 9–14 сот.</div>
                                    <div><span class="text-stone-400">Свет:</span> 15 кВт, оптика</div>
                                    <div><span class="text-stone-400">До КАД:</span> 25 минут</div>
                                </div>
                            </div>
                            <div class="flex items-center gap-3 pt-4 border-t border-stone-100">
                                <button onclick="openProjectModal('HYTTE', 'Всеволожский район', 'от 11.5 млн ₽', 'assets/hytte-house.jpg', 'Авторский проект Hygge в 25 минутах от КАД. Высокие потолки, терраса 30 м2, камин, подземный оптоволоконный интернет, прямой договор с Ленэнерго.')" class="btn-spring flex-1 py-3 px-4 rounded-xl bg-forest-900 hover:bg-forest-800 text-white font-mono text-xs uppercase tracking-wider text-center font-semibold">
                                    Генплан и планировка
                                </button>
                                <button onclick="openModal('vipModal')" title="Записаться на просмотр" class="btn-spring p-3 rounded-xl bg-stone-100 hover:bg-stone-200 text-forest-900 border border-stone-200">
                                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
                                </button>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Card 4: Юрки -->
                <div class="catalog-card" data-category="yurki">
                    <div class="bg-white rounded-3xl overflow-hidden border border-stone-200/90 shadow-elevation-card hover:shadow-elevation-hover transition-all duration-300 flex flex-col h-full group">
                        <div class="relative h-72 overflow-hidden bg-nordic-900">
                            <img src="assets/yurki-cottage.jpg" alt="Юрки" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 ease-out">
                            <div class="absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-black/20"></div>
                            <div class="absolute top-4 left-4 flex flex-wrap gap-2">
                                <span class="px-3 py-1 rounded-full text-[11px] font-mono uppercase tracking-wider bg-white/90 backdrop-blur-md text-nordic-900 font-semibold">ИЖС</span>
                                <span class="px-3 py-1 rounded-full text-[11px] font-mono uppercase tracking-wider bg-forest-900/90 backdrop-blur-md text-brass-300">Берег реки Луга</span>
                            </div>
                            <div class="absolute bottom-4 left-4 right-4 flex items-end justify-between text-white">
                                <div>
                                    <div class="text-xs font-mono text-stone-300 uppercase">Кингисеппский район</div>
                                    <h3 class="font-serif text-2xl font-bold">Юрки</h3>
                                </div>
                                <div class="text-right">
                                    <div class="text-xs font-mono text-brass-300">от 8 900 000 ₽</div>
                                    <div class="text-[10px] text-stone-300 font-mono">от 42 700 ₽/мес</div>
                                </div>
                            </div>
                        </div>
                        <div class="p-6 flex-1 flex flex-col justify-between">
                            <div>
                                <p class="text-xs text-stone-600 leading-relaxed mb-4">
                                    Уединённые эко-резиденции на первой береговой линии реки Луга. Первозданная природа, чистейшая вода, рыбалка и максимальная тишина.
                                </p>
                                <div class="grid grid-cols-2 gap-2 text-xs font-mono text-stone-700 mb-6 bg-stone-50 p-3 rounded-2xl border border-stone-100">
                                    <div><span class="text-stone-400">Площадь:</span> 95–140 м²</div>
                                    <div><span class="text-stone-400">Участки:</span> от 15 сот.</div>
                                    <div><span class="text-stone-400">Берег реки:</span> 50 метров</div>
                                    <div><span class="text-stone-400">Свет:</span> 15 кВт Ленэнерго</div>
                                </div>
                            </div>
                            <div class="flex items-center gap-3 pt-4 border-t border-stone-100">
                                <button onclick="openProjectModal('Юрки', 'Кингисеппский район, берег р. Луга', 'от 8.9 млн ₽', 'assets/yurki-cottage.jpg', 'Экологический оазис для ценителей природы и рыбалки. Большие лесные участки от 15 соток прямо у реки Луга, готовые коттеджи под ключ.')" class="btn-spring flex-1 py-3 px-4 rounded-xl bg-forest-900 hover:bg-forest-800 text-white font-mono text-xs uppercase tracking-wider text-center font-semibold">
                                    Генплан и планировка
                                </button>
                                <button onclick="openModal('vipModal')" title="Записаться на просмотр" class="btn-spring p-3 rounded-xl bg-stone-100 hover:bg-stone-200 text-forest-900 border border-stone-200">
                                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
                                </button>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Card 5: Scandi Barn 124 -->
                <div class="catalog-card" data-category="barn">
                    <div class="bg-white rounded-3xl overflow-hidden border border-stone-200/90 shadow-elevation-card hover:shadow-elevation-hover transition-all duration-300 flex flex-col h-full group">
                        <div class="relative h-72 overflow-hidden bg-nordic-900">
                            <img src="assets/barnhouse_scandi.jpg" alt="Scandi Barn 124" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 ease-out">
                            <div class="absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-black/20"></div>
                            <div class="absolute top-4 left-4 flex flex-wrap gap-2">
                                <span class="px-3 py-1 rounded-full text-[11px] font-mono uppercase tracking-wider bg-brass-500/90 backdrop-blur-md text-nordic-950 font-bold">Хит продаж</span>
                                <span class="px-3 py-1 rounded-full text-[11px] font-mono uppercase tracking-wider bg-white/90 backdrop-blur-md text-nordic-900 font-semibold">90 000 ₽/м²</span>
                            </div>
                            <div class="absolute bottom-4 left-4 right-4 flex items-end justify-between text-white">
                                <div>
                                    <div class="text-xs font-mono text-stone-300 uppercase">Архитектурный проект</div>
                                    <h3 class="font-serif text-2xl font-bold">Scandi Barn 124</h3>
                                </div>
                                <div class="text-right">
                                    <div class="text-xs font-mono text-brass-300">11 160 000 ₽</div>
                                    <div class="text-[10px] text-stone-300 font-mono">под ключ с участком</div>
                                </div>
                            </div>
                        </div>
                        <div class="p-6 flex-1 flex flex-col justify-between">
                            <div>
                                <p class="text-xs text-stone-600 leading-relaxed mb-4">
                                    Флагманский проект загородного дома: 3 изолированные спальни, просторная кухня-гостиная 38 м² с потолками 4.8 м и открытая терраса.
                                </p>
                                <div class="grid grid-cols-2 gap-2 text-xs font-mono text-stone-700 mb-6 bg-stone-50 p-3 rounded-2xl border border-stone-100">
                                    <div><span class="text-stone-400">Площадь:</span> 124 м²</div>
                                    <div><span class="text-stone-400">Спален:</span> 3 комнаты</div>
                                    <div><span class="text-stone-400">Терраса:</span> 28 м²</div>
                                    <div><span class="text-stone-400">Срок стройки:</span> 90 дней</div>
                                </div>
                            </div>
                            <div class="flex items-center gap-3 pt-4 border-t border-stone-100">
                                <button onclick="openProjectModal('Scandi Barn 124', 'Строится в любом из наших посёлков', '11.16 млн ₽ под ключ', 'assets/barnhouse_scandi.jpg', 'Флагманский дом 124 м2 с чистовой отделкой: энергосберегающие окна, монолитная плита с тёплым полом, 3 спальни, 2 санузла, кухня-гостиная со вторым светом.')" class="btn-spring flex-1 py-3 px-4 rounded-xl bg-forest-900 hover:bg-forest-800 text-white font-mono text-xs uppercase tracking-wider text-center font-semibold">
                                    Генплан и планировка
                                </button>
                                <button onclick="openModal('vipModal')" title="Записаться на просмотр" class="btn-spring p-3 rounded-xl bg-stone-100 hover:bg-stone-200 text-forest-900 border border-stone-200">
                                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
                                </button>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Card 6: Sawoda Terrace Villa 150 -->
                <div class="catalog-card" data-category="sawoda">
                    <div class="bg-white rounded-3xl overflow-hidden border border-stone-200/90 shadow-elevation-card hover:shadow-elevation-hover transition-all duration-300 flex flex-col h-full group">
                        <div class="relative h-72 overflow-hidden bg-nordic-900">
                            <img src="assets/sawoda-terrace-v3.png" alt="Sawoda Panoramic Villa" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 ease-out">
                            <div class="absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-black/20"></div>
                            <div class="absolute top-4 left-4 flex flex-wrap gap-2">
                                <span class="px-3 py-1 rounded-full text-[11px] font-mono uppercase tracking-wider bg-white/90 backdrop-blur-md text-nordic-900 font-semibold">ИЖС</span>
                                <span class="px-3 py-1 rounded-full text-[11px] font-mono uppercase tracking-wider bg-forest-900/90 backdrop-blur-md text-brass-300">Второй свет 5.8 м</span>
                            </div>
                            <div class="absolute bottom-4 left-4 right-4 flex items-end justify-between text-white">
                                <div>
                                    <div class="text-xs font-mono text-stone-300 uppercase">Архитектурный проект</div>
                                    <h3 class="font-serif text-2xl font-bold">Panoramic Villa 150</h3>
                                </div>
                                <div class="text-right">
                                    <div class="text-xs font-mono text-brass-300">от 13 500 000 ₽</div>
                                    <div class="text-[10px] text-stone-300 font-mono">от 64 900 ₽/мес</div>
                                </div>
                            </div>
                        </div>
                        <div class="p-6 flex-1 flex flex-col justify-between">
                            <div>
                                <p class="text-xs text-stone-600 leading-relaxed mb-4">
                                    Панорамная загородная резиденция с мастер-спальней, гардеробной комнатой, крытой террасой для барбекю и панорамным остеклением в пол.
                                </p>
                                <div class="grid grid-cols-2 gap-2 text-xs font-mono text-stone-700 mb-6 bg-stone-50 p-3 rounded-2xl border border-stone-100">
                                    <div><span class="text-stone-400">Площадь:</span> 150 м²</div>
                                    <div><span class="text-stone-400">Спален:</span> 4 спальни</div>
                                    <div><span class="text-stone-400">Окна:</span> Guardian Glass</div>
                                    <div><span class="text-stone-400">Отделка:</span> Чистовая под ключ</div>
                                </div>
                            </div>
                            <div class="flex items-center gap-3 pt-4 border-t border-stone-100">
                                <button onclick="openProjectModal('Panoramic Villa 150', 'КП Sawoda / КП Honkaniemi', 'от 13.5 млн ₽', 'assets/sawoda-terrace-v3.png', 'Премиальная вилла с мастер-спальней и террасой. Просторная кухня-гостиная с выходом в приватный сад, монолитный водяной тёплый пол, чистовая дизайнерская отделка.')" class="btn-spring flex-1 py-3 px-4 rounded-xl bg-forest-900 hover:bg-forest-800 text-white font-mono text-xs uppercase tracking-wider text-center font-semibold">
                                    Генплан и планировка
                                </button>
                                <button onclick="openModal('vipModal')" title="Записаться на просмотр" class="btn-spring p-3 rounded-xl bg-stone-100 hover:bg-stone-200 text-forest-900 border border-stone-200">
                                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    '''

def get_manifesto():
    return '''
    <!-- Manifesto of Quality & Unfair Advantages (Bento Grid) -->
    <section id="standards" class="py-24 sm:py-32 bg-nordic-900 text-white relative overflow-hidden">
        <!-- Ambient Atmospheric Glows -->
        <div class="absolute -top-40 -right-40 w-96 h-96 bg-forest-600/20 rounded-full blur-[140px] pointer-events-none"></div>
        <div class="absolute -bottom-40 -left-40 w-96 h-96 bg-brass-500/15 rounded-full blur-[140px] pointer-events-none"></div>

        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <!-- Header -->
            <div class="max-w-3xl mb-16 sm:mb-20">
                <div class="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-forest-800/80 border border-forest-600/50 text-xs font-mono text-brass-300 uppercase tracking-widest mb-4">
                    <span>Стандарты девелопмента</span>
                </div>
                <h2 class="text-3xl sm:text-5xl font-serif text-white tracking-tight leading-tight">
                    Почему выбирают нас: <span class="italic text-brass-300">4 фундаментальных преимущества.</span>
                </h2>
                <p class="text-base text-stone-400 font-light mt-4">
                    Мы убрали все риски и бюрократические барьеры, превратив покупку загородного дома в предсказуемый и комфортный процесс.
                </p>
            </div>

            <!-- Bento Grid -->
            <div class="grid grid-cols-1 md:grid-cols-12 gap-6 sm:gap-8">
                <!-- Bento 1: Large Span - Строим на собственный капитал -->
                <div class="md:col-span-7 bg-nordic-850 rounded-3xl p-8 sm:p-12 border border-white/10 hover:border-brass-400/50 transition-all duration-300 relative overflow-hidden flex flex-col justify-between group">
                    <div class="absolute -right-12 -bottom-12 w-64 h-64 bg-forest-700/20 rounded-full blur-3xl pointer-events-none group-hover:bg-brass-500/20 transition-all duration-500"></div>
                    <div>
                        <div class="flex items-center justify-between mb-8">
                            <span class="px-3.5 py-1 rounded-full text-xs font-mono uppercase tracking-wider bg-brass-500/20 text-brass-300 border border-brass-500/40 font-semibold">
                                Главный аргумент
                            </span>
                            <span class="font-serif text-3xl text-white/30 font-light">01</span>
                        </div>
                        <h3 class="text-2xl sm:text-4xl font-serif text-white mb-4 leading-snug">
                            Строим на <span class="text-brass-300">собственный капитал</span> компании
                        </h3>
                        <p class="text-stone-300 text-sm sm:text-base leading-relaxed mb-6 font-light">
                            В отличие от большинства застройщиков, мы не зависим от задержек банковских траншей и раскрытия эскроу-счетов. Строительная техника и материалы заезжают на участок через 7 дней после подписания договора. Дома сдаются на 1.5–2 месяца быстрее рынка.
                        </p>
                    </div>
                    <div class="grid grid-cols-2 gap-4 pt-6 border-t border-white/10 text-xs font-mono text-stone-300">
                        <div>
                            <div class="text-xl sm:text-2xl font-serif text-white font-bold mb-1">7 дней</div>
                            <div class="text-stone-400 text-[11px]">до выхода бригады на площадку</div>
                        </div>
                        <div>
                            <div class="text-xl sm:text-2xl font-serif text-brass-300 font-bold mb-1">0 дней</div>
                            <div class="text-stone-400 text-[11px]">задержек из-за согласований банков</div>
                        </div>
                    </div>
                </div>

                <!-- Bento 2: Синхронный Trade-In -->
                <div class="md:col-span-5 bg-nordic-850 rounded-3xl p-8 sm:p-10 border border-white/10 hover:border-brass-400/50 transition-all duration-300 flex flex-col justify-between group">
                    <div>
                        <div class="flex items-center justify-between mb-6">
                            <span class="px-3 py-1 rounded-full text-xs font-mono uppercase tracking-wider bg-white/10 text-stone-300 border border-white/15">
                                Без съёмного жилья
                            </span>
                            <span class="font-serif text-3xl text-white/30 font-light">02</span>
                        </div>
                        <h3 class="text-2xl font-serif text-white mb-3">Синхронный Trade-In</h3>
                        <p class="text-stone-300 text-xs sm:text-sm leading-relaxed mb-6 font-light">
                            Принимаем вашу квартиру в зачет нового дома. Вы не переезжаете на чемоданах и не платите за аренду: продолжаете спокойно жить в своей квартире до момента передачи ключей и завершения чистовой отделки!
                        </p>
                    </div>
                    <div class="p-4 rounded-2xl bg-white/5 border border-white/10 text-xs font-mono text-brass-300">
                        Оценка квартиры за 24 часа · Юридическое сопровождение сделки
                    </div>
                </div>

                <!-- Bento 3: Заводской энергоэффективный тёплый контур -->
                <div class="md:col-span-5 bg-nordic-850 rounded-3xl p-8 sm:p-10 border border-white/10 hover:border-brass-400/50 transition-all duration-300 flex flex-col justify-between group">
                    <div>
                        <div class="flex items-center justify-between mb-6">
                            <span class="px-3 py-1 rounded-full text-xs font-mono uppercase tracking-wider bg-white/10 text-stone-300 border border-white/15">
                                Энергоэффективность A+
                            </span>
                            <span class="font-serif text-3xl text-white/30 font-light">03</span>
                        </div>
                        <h3 class="text-2xl font-serif text-white mb-3">Тёплый контур под ключ</h3>
                        <p class="text-stone-300 text-xs sm:text-sm leading-relaxed mb-6 font-light">
                            Монолитная армированная плита со встроенным водяным тёплым полом. Двойное перекрёстное утепление 250 мм Rockwool. Двухкамерные стеклопакеты Guardian Glass с аргоном.
                        </p>
                    </div>
                    <div class="p-4 rounded-2xl bg-white/5 border border-white/10 text-xs font-mono text-emerald-400">
                        Экономия до 40% на отоплении в зимний период
                    </div>
                </div>

                <!-- Bento 4: 100% готовые коммуникации -->
                <div class="md:col-span-7 bg-nordic-850 rounded-3xl p-8 sm:p-12 border border-white/10 hover:border-brass-400/50 transition-all duration-300 relative overflow-hidden flex flex-col justify-between group">
                    <div>
                        <div class="flex items-center justify-between mb-8">
                            <span class="px-3.5 py-1 rounded-full text-xs font-mono uppercase tracking-wider bg-forest-700/80 text-emerald-300 border border-forest-600/50 font-semibold">
                                Всё включено в договор
                            </span>
                            <span class="font-serif text-3xl text-white/30 font-light">04</span>
                        </div>
                        <h3 class="text-2xl sm:text-4xl font-serif text-white mb-4 leading-snug">
                            100% инженерных сетей <span class="text-brass-300">уже в стоимости</span>
                        </h3>
                        <p class="text-stone-300 text-sm sm:text-base leading-relaxed mb-6 font-light">
                            Никаких "под ключ с доплатами за свет и газ": 15 кВт электричества с прямым договором Ленэнерго, магистральный газ заведён в дом, индивидуальная артезианская скважина, станция биоочистки и скоростное подземное оптоволокно.
                        </p>
                    </div>
                    <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 pt-6 border-t border-white/10 text-xs font-mono text-stone-300">
                        <div class="p-2.5 rounded-xl bg-white/5 border border-white/5 text-center">
                            <div class="text-brass-300 font-bold mb-0.5">15 кВт</div>
                            <div class="text-[10px] text-stone-400">Ленэнерго</div>
                        </div>
                        <div class="p-2.5 rounded-xl bg-white/5 border border-white/5 text-center">
                            <div class="text-brass-300 font-bold mb-0.5">Газ</div>
                            <div class="text-[10px] text-stone-400">Магистральный</div>
                        </div>
                        <div class="p-2.5 rounded-xl bg-white/5 border border-white/5 text-center">
                            <div class="text-brass-300 font-bold mb-0.5">Вода</div>
                            <div class="text-[10px] text-stone-400">Скважина</div>
                        </div>
                        <div class="p-2.5 rounded-xl bg-white/5 border border-white/5 text-center">
                            <div class="text-brass-300 font-bold mb-0.5">Оптика</div>
                            <div class="text-[10px] text-stone-400">До 500 Мбит/с</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    '''

def get_calculator():
    return '''
    <!-- Interactive Mortgage Engineering Lab 2026 -->
    <section id="calculator" class="py-24 sm:py-32 bg-stone-100 border-b border-stone-200/80">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <!-- Header -->
            <div class="flex flex-col md:flex-row md:items-end justify-between mb-16 sm:mb-20">
                <div class="max-w-2xl">
                    <div class="text-xs font-mono uppercase tracking-widest text-forest-700 font-semibold mb-3">
                        Финансовая лаборатория 2026
                    </div>
                    <h2 class="text-3xl sm:text-5xl font-serif text-nordic-900 tracking-tight leading-tight">
                        Интерактивный расчёт ипотеки <span class="italic text-forest-600">с актуальными лимитами.</span>
                    </h2>
                </div>
                <div class="mt-4 md:mt-0 text-xs font-mono text-stone-500 bg-white px-4 py-2 rounded-full border border-stone-200 shadow-sm">
                    Аккредитация: Сбербанк · ВТБ · ДОМ.РФ · Альфа
                </div>
            </div>

            <!-- Main Calculator Card -->
            <div class="bg-white rounded-3xl border border-stone-200/90 shadow-elevation-hover p-6 sm:p-10 lg:p-12">
                <!-- Program Switcher Tabs -->
                <div class="mb-10">
                    <div class="text-xs font-mono uppercase tracking-wider text-stone-500 mb-3">Выберите программу:</div>
                    <div class="grid grid-cols-2 md:grid-cols-4 gap-3 p-1.5 rounded-2xl bg-stone-100 border border-stone-200">
                        <button onclick="setProgram('family')" id="progBtnFamily" class="calc-prog-btn active p-3 rounded-xl text-left transition-all duration-200 bg-forest-900 text-white shadow-md">
                            <div class="flex items-center justify-between mb-1">
                                <span class="font-serif text-sm font-bold">Семейная</span>
                                <span class="text-xs font-mono text-brass-300">6.0%</span>
                            </div>
                            <div class="text-[11px] text-stone-300 font-mono">Лимит 12 млн ₽</div>
                        </button>

                        <button onclick="setProgram('it')" id="progBtnIT" class="calc-prog-btn p-3 rounded-xl text-left transition-all duration-200 text-stone-700 hover:bg-stone-200/70">
                            <div class="flex items-center justify-between mb-1">
                                <span class="font-serif text-sm font-bold">IT в ЛО</span>
                                <span class="text-xs font-mono text-emerald-700">6.0%</span>
                            </div>
                            <div class="text-[11px] text-stone-500 font-mono">Лимит 9 млн ₽</div>
                        </button>

                        <button onclick="setProgram('base')" id="progBtnBase" class="calc-prog-btn p-3 rounded-xl text-left transition-all duration-200 text-stone-700 hover:bg-stone-200/70">
                            <div class="flex items-center justify-between mb-1">
                                <span class="font-serif text-sm font-bold">Базовая</span>
                                <span class="text-xs font-mono text-stone-600">23.0%</span>
                            </div>
                            <div class="text-[11px] text-stone-500 font-mono">Без лимита субсидии</div>
                        </button>

                        <button onclick="setProgram('tradein')" id="progBtnTradein" class="calc-prog-btn p-3 rounded-xl text-left transition-all duration-200 text-stone-700 hover:bg-stone-200/70">
                            <div class="flex items-center justify-between mb-1">
                                <span class="font-serif text-sm font-bold">Trade-In</span>
                                <span class="text-xs font-mono text-brass-600">Зачет</span>
                            </div>
                            <div class="text-[11px] text-stone-500 font-mono">Квартира в СПб</div>
                        </button>
                    </div>
                </div>

                <!-- Program Description Banner -->
                <div id="programBanner" class="p-4 rounded-2xl bg-forest-900/5 border border-forest-900/10 mb-10 flex items-start space-x-3 text-xs sm:text-sm text-stone-700 leading-relaxed font-sans">
                    <svg class="w-5 h-5 text-forest-700 flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                    <div id="programDescription">
                        <strong class="text-nordic-900">Семейная ипотека 6%:</strong> Лимит субсидии в Ленинградской области до 12 000 000 ₽. Доступна семьям с ребенком в возрасте до 6 лет включительно. Первоначальный взнос от 20%.
                    </div>
                </div>

                <!-- Sliders & Output Layout -->
                <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
                    <!-- Left: Sliders (7 Cols) -->
                    <div class="lg:col-span-7 space-y-8">
                        <!-- Slider 1: Стоимость дома -->
                        <div>
                            <div class="flex items-center justify-between mb-2">
                                <label class="text-xs font-mono uppercase tracking-wider text-stone-600">Стоимость дома с участком:</label>
                                <span id="priceVal" class="font-mono text-lg font-bold text-nordic-900">12 400 000 ₽</span>
                            </div>
                            <input type="range" id="priceRange" min="6000000" max="35000000" step="100000" value="12400000" class="w-full">
                            <div class="flex justify-between text-[11px] font-mono text-stone-400 mt-1">
                                <span>6 млн ₽</span>
                                <span>35 млн ₽</span>
                            </div>
                        </div>

                        <!-- Slider 2: Первоначальный взнос -->
                        <div>
                            <div class="flex items-center justify-between mb-2">
                                <label class="text-xs font-mono uppercase tracking-wider text-stone-600">Первоначальный взнос:</label>
                                <span id="downVal" class="font-mono text-lg font-bold text-nordic-900">2 480 000 ₽ (20%)</span>
                            </div>
                            <input type="range" id="downRange" min="20" max="80" step="1" value="20" class="w-full">
                            <div class="flex justify-between text-[11px] font-mono text-stone-400 mt-1">
                                <span>20% (мин.)</span>
                                <span>80%</span>
                            </div>
                        </div>

                        <!-- Slider 3: Срок кредита -->
                        <div>
                            <div class="flex items-center justify-between mb-2">
                                <label class="text-xs font-mono uppercase tracking-wider text-stone-600">Срок кредитования:</label>
                                <span id="yearsVal" class="font-mono text-lg font-bold text-nordic-900">30 лет</span>
                            </div>
                            <input type="range" id="yearsRange" min="5" max="30" step="1" value="30" class="w-full">
                            <div class="flex justify-between text-[11px] font-mono text-stone-400 mt-1">
                                <span>5 лет</span>
                                <span>30 лет</span>
                            </div>
                        </div>

                        <!-- Combo Mortgage Alert (Hidden by default) -->
                        <div id="comboAlert" class="hidden p-4 rounded-2xl bg-amber-50 border border-amber-200 text-xs text-amber-900 flex items-start space-x-2">
                            <svg class="w-4 h-4 text-amber-600 flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/></svg>
                            <div>
                                <strong>Комбинированная ипотека:</strong> Сумма кредита превышает субсидированный лимит программы. Расчёт произведён по льготной ставке 6% на максимальный лимит + рыночная ставка на превышение.
                            </div>
                        </div>
                    </div>

                    <!-- Right: Dynamic Results Box with SVG Donut (5 Cols) -->
                    <div class="lg:col-span-5 bg-nordic-900 text-white rounded-3xl p-6 sm:p-8 border border-white/10 shadow-2xl flex flex-col justify-between">
                        <div>
                            <div class="flex items-center justify-between pb-4 border-b border-white/10 mb-6">
                                <span class="text-xs font-mono uppercase tracking-wider text-stone-400">Сумма займа:</span>
                                <span id="loanSum" class="font-mono text-base font-bold text-white">9 920 000 ₽</span>
                            </div>

                            <!-- Live Monthly Payment Big Display -->
                            <div class="mb-6">
                                <div class="text-xs font-mono uppercase tracking-wider text-brass-400 mb-1">Ежемесячный платёж:</div>
                                <div id="monthlyPayment" class="text-4xl sm:text-5xl font-serif text-white font-bold tracking-tight">59 475 ₽</div>
                                <div class="text-[11px] text-stone-400 font-mono mt-1">аннуитетный платёж</div>
                            </div>

                            <!-- Additional Metrics: Income & Savings -->
                            <div class="space-y-3 mb-8 pt-4 border-t border-white/10 text-xs font-mono">
                                <div class="flex justify-between items-center text-stone-300">
                                    <span class="text-stone-400">Необходимый доход:</span>
                                    <span id="incomeNeeded" class="text-white font-semibold">от 118 000 ₽/мес</span>
                                </div>
                                <div class="flex justify-between items-center text-stone-300">
                                    <span class="text-stone-400">Экономия с 6%:</span>
                                    <span id="savingsVal" class="text-emerald-400 font-semibold">до 14 200 000 ₽</span>
                                </div>
                            </div>
                        </div>

                        <!-- CTA Button -->
                        <button onclick="openModal('calcLeadModal')" class="btn-spring w-full py-4 rounded-2xl bg-brass-500 hover:bg-brass-400 text-nordic-950 font-semibold text-xs tracking-wider uppercase text-center shadow-glow-brass flex items-center justify-center space-x-2">
                            <span>Одобрить ипотеку за 24 часа</span>
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </section>
    '''

def get_comparison_matrix():
    return '''
    <!-- Architectural Comparison Matrix of 4 Settlements -->
    <section class="py-24 sm:py-32 bg-stone-50 border-b border-stone-200/80">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="max-w-3xl mb-16 sm:mb-20">
                <div class="text-xs font-mono uppercase tracking-widest text-forest-700 font-semibold mb-3">
                    Архитектурный гид
                </div>
                <h2 class="text-3xl sm:text-5xl font-serif text-nordic-900 tracking-tight leading-tight">
                    Сравнение посёлков: <span class="italic text-forest-600">найдите идеальную локацию.</span>
                </h2>
                <p class="text-base text-stone-600 font-light mt-4">
                    Каждый посёлок обладает уникальным природным ландшафтом и концепцией застройки.
                </p>
            </div>

            <!-- Comparison Table Container with Horizontal Scroll on Mobile -->
            <div class="overflow-x-auto pb-4">
                <div class="min-w-[800px] bg-white rounded-3xl border border-stone-200/90 shadow-elevation-card overflow-hidden">
                    <table class="w-full text-left text-xs font-mono">
                        <thead>
                            <tr class="bg-nordic-900 text-white">
                                <th class="p-6 font-serif text-base uppercase tracking-wider">Параметр</th>
                                <th class="p-6 font-serif text-base text-brass-300">Honkaniemi</th>
                                <th class="p-6 font-serif text-base text-brass-300">Sawoda</th>
                                <th class="p-6 font-serif text-base text-brass-300">HYTTE</th>
                                <th class="p-6 font-serif text-base text-brass-300">Юрки</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-stone-100 text-stone-700">
                            <tr class="hover:bg-stone-50/80 transition-colors">
                                <td class="p-5 font-semibold text-nordic-900 bg-stone-50/50">Район ЛО</td>
                                <td class="p-5">Выборгский р-н (Карельский перешеек)</td>
                                <td class="p-5">Тосненский р-н</td>
                                <td class="p-5">Всеволожский р-н</td>
                                <td class="p-5">Кингисеппский р-н</td>
                            </tr>
                            <tr class="hover:bg-stone-50/80 transition-colors">
                                <td class="p-5 font-semibold text-nordic-900 bg-stone-50/50">Природный ландшафт</td>
                                <td class="p-5">Вековой сосновый бор, система озёр</td>
                                <td class="p-5">Березовая роща, закрытый клубный парк</td>
                                <td class="p-5">Хвойный лес, концепция Hygge</td>
                                <td class="p-5">Первая линия реки Луга, реликтовый лес</td>
                            </tr>
                            <tr class="hover:bg-stone-50/80 transition-colors">
                                <td class="p-5 font-semibold text-nordic-900 bg-stone-50/50">Время в пути до КАД</td>
                                <td class="p-5">45 минут по трассе Скандинавия</td>
                                <td class="p-5">35 минут по М-11 / Московскому шоссе</td>
                                <td class="p-5 text-emerald-700 font-bold">25 минут</td>
                                <td class="p-5">65 минут</td>
                            </tr>
                            <tr class="hover:bg-stone-50/80 transition-colors">
                                <td class="p-5 font-semibold text-nordic-900 bg-stone-50/50">Площадь участков</td>
                                <td class="p-5">12–25 соток</td>
                                <td class="p-5">8–15 соток</td>
                                <td class="p-5">9–14 соток</td>
                                <td class="p-5 text-emerald-700 font-bold">от 15 до 30 соток</td>
                            </tr>
                            <tr class="hover:bg-stone-50/80 transition-colors">
                                <td class="p-5 font-semibold text-nordic-900 bg-stone-50/50">Газификация</td>
                                <td class="p-5">Магистральный газ</td>
                                <td class="p-5">Магистральный газ</td>
                                <td class="p-5">Электрическое (газ 2026)</td>
                                <td class="p-5">Индивидуальное</td>
                            </tr>
                            <tr class="hover:bg-stone-50/80 transition-colors">
                                <td class="p-5 font-semibold text-nordic-900 bg-stone-50/50">Архитектурный стиль</td>
                                <td class="p-5">Фахверк и Scandi-Modern</td>
                                <td class="p-5">Nordic Barnhouse</td>
                                <td class="p-5">Minimalist Black Hygge</td>
                                <td class="p-5">Эко-резиденции</td>
                            </tr>
                            <tr class="hover:bg-stone-50/80 transition-colors bg-brass-50/30">
                                <td class="p-5 font-semibold text-nordic-900 bg-stone-50/50">Стоимость дома с участком</td>
                                <td class="p-5 font-bold text-forest-900 text-sm">от 14.8 млн ₽</td>
                                <td class="p-5 font-bold text-forest-900 text-sm">от 9.9 млн ₽</td>
                                <td class="p-5 font-bold text-forest-900 text-sm">от 11.5 млн ₽</td>
                                <td class="p-5 font-bold text-forest-900 text-sm">от 8.9 млн ₽</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </section>
    '''

def get_faq():
    return '''
    <!-- FAQ Section with Smooth CSS Grid Accordion -->
    <section id="faq" class="py-24 sm:py-32 bg-stone-100 border-b border-stone-200/80">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center max-w-2xl mx-auto mb-16 sm:mb-20">
                <div class="text-xs font-mono uppercase tracking-widest text-forest-700 font-semibold mb-3">
                    Юридическая прозрачность
                </div>
                <h2 class="text-3xl sm:text-5xl font-serif text-nordic-900 tracking-tight leading-tight">
                    Ответы на главные вопросы <span class="italic text-forest-600">покупателей.</span>
                </h2>
            </div>

            <!-- Accordion List -->
            <div class="space-y-4">
                <!-- FAQ 1 -->
                <div class="accordion-item bg-white rounded-2xl border border-stone-200/90 shadow-sm overflow-hidden transition-all duration-300">
                    <button class="accordion-toggle w-full p-6 text-left flex items-center justify-between space-x-4">
                        <span class="font-serif text-lg sm:text-xl font-bold text-nordic-900">Какой юридический статус земли и оформляется ли она в собственность?</span>
                        <div class="accordion-icon w-8 h-8 rounded-full bg-stone-100 flex items-center justify-center flex-shrink-0 text-forest-800 transition-transform duration-300">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/></svg>
                        </div>
                    </button>
                    <div class="accordion-content px-6 pb-6 text-stone-600 text-sm leading-relaxed">
                        <div class="overflow-hidden pt-2 border-t border-stone-100">
                            Земля имеет статус ИЖС (индивидуальное жилищное строительство). Каждый земельный участок имеет индивидуальный кадастровый номер и оформляется в вашу прямую частную собственность через регистрацию в Росреестре. Вы получаете право постоянной регистрации (прописки) и почтовый адрес.
                        </div>
                    </div>
                </div>

                <!-- FAQ 2 -->
                <div class="accordion-item bg-white rounded-2xl border border-stone-200/90 shadow-sm overflow-hidden transition-all duration-300">
                    <button class="accordion-toggle w-full p-6 text-left flex items-center justify-between space-x-4">
                        <span class="font-serif text-lg sm:text-xl font-bold text-nordic-900">Как работает синхронный Trade-In и когда мне освобождать свою квартиру?</span>
                        <div class="accordion-icon w-8 h-8 rounded-full bg-stone-100 flex items-center justify-center flex-shrink-0 text-forest-800 transition-transform duration-300">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/></svg>
                        </div>
                    </button>
                    <div class="accordion-content px-6 pb-6 text-stone-600 text-sm leading-relaxed">
                        <div class="overflow-hidden pt-2 border-t border-stone-100">
                            Мы оцениваем вашу квартиру по рыночной стоимости за 24 часа. Стоимость квартиры фиксируется в договоре и засчитывается в оплату загородного дома. При этом вы продолжаете проживать в своей квартире до момента завершения чистовой отделки и торжественной передачи ключей от дома. Никакой необходимости снимать временное жильё!
                        </div>
                    </div>
                </div>

                <!-- FAQ 3 -->
                <div class="accordion-item bg-white rounded-2xl border border-stone-200/90 shadow-sm overflow-hidden transition-all duration-300">
                    <button class="accordion-toggle w-full p-6 text-left flex items-center justify-between space-x-4">
                        <span class="font-serif text-lg sm:text-xl font-bold text-nordic-900">За счет чего вы начинаете стройку за 7 дней и строите быстрее рынка?</span>
                        <div class="accordion-icon w-8 h-8 rounded-full bg-stone-100 flex items-center justify-center flex-shrink-0 text-forest-800 transition-transform duration-300">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/></svg>
                        </div>
                    </button>
                    <div class="accordion-content px-6 pb-6 text-stone-600 text-sm leading-relaxed">
                        <div class="overflow-hidden pt-2 border-t border-stone-100">
                            Девелопер «АТС Малиновка» финансирует строительство из собственного оборотного капитала, сформированного за 15 лет успешной работы. Мы не зависим от ожидания траншей банковского проектного финансирования. Бригада и собственная спецтехника заезжают на объект сразу после подписания договора подряда.
                        </div>
                    </div>
                </div>

                <!-- FAQ 4 -->
                <div class="accordion-item bg-white rounded-2xl border border-stone-200/90 shadow-sm overflow-hidden transition-all duration-300">
                    <button class="accordion-toggle w-full p-6 text-left flex items-center justify-between space-x-4">
                        <span class="font-serif text-lg sm:text-xl font-bold text-nordic-900">Какие гарантии предоставляются на дом и фиксируется ли цена в договоре?</span>
                        <div class="accordion-icon w-8 h-8 rounded-full bg-stone-100 flex items-center justify-center flex-shrink-0 text-forest-800 transition-transform duration-300">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/></svg>
                        </div>
                    </button>
                    <div class="accordion-content px-6 pb-6 text-stone-600 text-sm leading-relaxed">
                        <div class="overflow-hidden pt-2 border-t border-stone-100">
                            Цена дома и участка строго фиксируется в договоре подряда в рублях и не подлежит увеличению в процессе строительства. На несущий силовой каркас и монолитный фундамент действует официальная гарантия 10 лет, на инженерные сети и кровлю — 5 лет.
                        </div>
                    </div>
                </div>

                <!-- FAQ 5 -->
                <div class="accordion-item bg-white rounded-2xl border border-stone-200/90 shadow-sm overflow-hidden transition-all duration-300">
                    <button class="accordion-toggle w-full p-6 text-left flex items-center justify-between space-x-4">
                        <span class="font-serif text-lg sm:text-xl font-bold text-nordic-900">Что входит в стоимость инженерии «под ключ»?</span>
                        <div class="accordion-icon w-8 h-8 rounded-full bg-stone-100 flex items-center justify-center flex-shrink-0 text-forest-800 transition-transform duration-300">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/></svg>
                        </div>
                    </button>
                    <div class="accordion-content px-6 pb-6 text-stone-600 text-sm leading-relaxed">
                        <div class="overflow-hidden pt-2 border-t border-stone-100">
                            В стоимость каждого дома входит: электричество 15 кВт с прямым абонентским договором Ленэнерго, магистральный газ (в посёлках с газификацией) с вводом в котельную, индивидуальная артезианская скважина с насосным оборудованием, станция биологической очистки стоков и система водяного тёплого пола по всему периметру.
                        </div>
                    </div>
                </div>

                <!-- FAQ 6 -->
                <div class="accordion-item bg-white rounded-2xl border border-stone-200/90 shadow-sm overflow-hidden transition-all duration-300">
                    <button class="accordion-toggle w-full p-6 text-left flex items-center justify-between space-x-4">
                        <span class="font-serif text-lg sm:text-xl font-bold text-nordic-900">Можно ли внести изменения в планировку типового проекта?</span>
                        <div class="accordion-icon w-8 h-8 rounded-full bg-stone-100 flex items-center justify-center flex-shrink-0 text-forest-800 transition-transform duration-300">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/></svg>
                        </div>
                    </button>
                    <div class="accordion-content px-6 pb-6 text-stone-600 text-sm leading-relaxed">
                        <div class="overflow-hidden pt-2 border-t border-stone-100">
                            Да! До начала строительных работ наш штатный архитектор бесплатно адаптирует внутреннюю планировку под задачи вашей семьи: добавит гардеробную, увеличит террасу, скорректирует расположение спален или сауны без удорожания базового конструктива.
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    '''

def get_about():
    return '''
    <!-- About Developer Section -->
    <section id="about" class="py-24 sm:py-32 bg-stone-50 border-b border-stone-200/80">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 sm:gap-16 items-center">
                <!-- Left: Big Editorial Image Frame -->
                <div class="lg:col-span-5 relative">
                    <div class="rounded-3xl overflow-hidden shadow-2xl border border-stone-300/80 relative">
                        <img src="assets/luxury_evening.jpg" alt="Evening Villa" class="w-full h-[480px] object-cover">
                        <div class="absolute inset-0 bg-gradient-to-t from-nordic-950/80 via-transparent to-transparent"></div>
                        <div class="absolute bottom-6 left-6 right-6 text-white">
                            <div class="text-xs font-mono text-brass-300 uppercase mb-1">С 2009 года в Ленинградской области</div>
                            <div class="font-serif text-2xl font-bold">АТС Малиновка</div>
                        </div>
                    </div>
                    <!-- Overlapping Heritage Badge -->
                    <div class="absolute -bottom-6 -right-6 bg-forest-900 text-white p-6 rounded-2xl border border-brass-500/40 shadow-xl hidden sm:block">
                        <div class="font-serif text-3xl font-bold text-brass-300">15+ лет</div>
                        <div class="text-[11px] font-mono text-stone-300 uppercase tracking-wider">безупречной репутации</div>
                    </div>
                </div>

                <!-- Right: Story & Facts -->
                <div class="lg:col-span-7">
                    <div class="text-xs font-mono uppercase tracking-widest text-forest-700 font-semibold mb-3">
                        О девелопере
                    </div>
                    <h2 class="text-3xl sm:text-5xl font-serif text-nordic-900 tracking-tight leading-tight mb-6">
                        Мы строим не просто квадратные метры, <span class="italic text-forest-600">а качество вашей жизни.</span>
                    </h2>
                    <p class="text-stone-600 text-base leading-relaxed mb-6 font-light">
                        Компания «АТС Малиновка» основана в 2009 году. За 15 лет работы мы превратились из камерного подрядчика в одного из самых надежных девелоперов загородной недвижимости Санкт-Петербурга и Ленинградской области.
                    </p>
                    <p class="text-stone-600 text-base leading-relaxed mb-8 font-light">
                        Наша философия проста: строить только из проверенных скандинавских материалов, сдавать дома точно в срок, полностью обеспечивать посёлки готовой инженерией и финансировать проекты собственным капиталом.
                    </p>

                    <!-- Real Metric Numbers -->
                    <div class="grid grid-cols-2 sm:grid-cols-4 gap-4 pt-6 border-t border-stone-200">
                        <div>
                            <div class="font-serif text-3xl sm:text-4xl font-bold text-forest-900">420+</div>
                            <div class="text-xs font-mono text-stone-500 mt-1">построенных домов</div>
                        </div>
                        <div>
                            <div class="font-serif text-3xl sm:text-4xl font-bold text-forest-900">5</div>
                            <div class="text-xs font-mono text-stone-500 mt-1">посёлков в портфеле</div>
                        </div>
                        <div>
                            <div class="font-serif text-3xl sm:text-4xl font-bold text-forest-900">100%</div>
                            <div class="text-xs font-mono text-stone-500 mt-1">объектов сдано в срок</div>
                        </div>
                        <div>
                            <div class="font-serif text-3xl sm:text-4xl font-bold text-forest-900">10 лет</div>
                            <div class="text-xs font-mono text-stone-500 mt-1">гарантия по договору</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    '''

def get_contact():
    return '''
    <!-- Final CTA & VIP Test-Drive Booking -->
    <section id="contact" class="py-24 sm:py-32 bg-nordic-950 text-white relative overflow-hidden">
        <!-- Ambient Atmosphere -->
        <div class="absolute -top-40 -left-40 w-96 h-96 bg-forest-600/20 rounded-full blur-[140px] pointer-events-none"></div>
        <div class="absolute -bottom-40 -right-40 w-96 h-96 bg-brass-500/15 rounded-full blur-[140px] pointer-events-none"></div>

        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 sm:gap-16 items-center">
                <!-- Left: Headline & Atmosphere -->
                <div class="lg:col-span-6">
                    <div class="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-brass-500/20 border border-brass-500/40 text-xs font-mono text-brass-300 uppercase tracking-widest mb-4">
                        <span>Индивидуальный сервис</span>
                    </div>
                    <h2 class="text-3xl sm:text-5xl font-serif text-white tracking-tight leading-tight mb-6">
                        Запишитесь на персональный <span class="italic text-brass-300">VIP тест-драйв</span> загородной жизни.
                    </h2>
                    <p class="text-stone-300 text-base leading-relaxed mb-8 font-light">
                        Мы бесплатно предоставим автомобиль бизнес-класса (Mercedes-Benz / Genesis) с личным водителем, который заберёт вас от дома или станции метро, привезёт в выбранный посёлок, где главный архитектор проекта проведёт экскурсию по готовым домам.
                    </p>

                    <!-- Feature Points -->
                    <div class="space-y-4 mb-8 text-xs font-mono text-stone-300">
                        <div class="flex items-center space-x-3">
                            <div class="w-6 h-6 rounded-full bg-brass-500/20 text-brass-300 flex items-center justify-center font-bold">✓</div>
                            <span>Трансфер на автомобиле бизнес-класса туда и обратно</span>
                        </div>
                        <div class="flex items-center space-x-3">
                            <div class="w-6 h-6 rounded-full bg-brass-500/20 text-brass-300 flex items-center justify-center font-bold">✓</div>
                            <span>Осмотр готовых и строящихся домов, чаепитие у камина</span>
                        </div>
                        <div class="flex items-center space-x-3">
                            <div class="w-6 h-6 rounded-full bg-brass-500/20 text-brass-300 flex items-center justify-center font-bold">✓</div>
                            <span>Индивидуальный расчет ипотеки и trade-in на месте</span>
                        </div>
                    </div>

                    <!-- Instant Messengers -->
                    <div class="flex flex-wrap items-center gap-4 pt-6 border-t border-white/10">
                        <span class="text-xs font-mono text-stone-400">Быстрая связь в мессенджерах:</span>
                        <div class="flex items-center gap-3">
                            <a href="https://t.me/" target="_blank" rel="noopener" class="btn-spring px-4 py-2 rounded-xl bg-white/10 hover:bg-white/20 text-white text-xs font-mono flex items-center space-x-2 border border-white/15">
                                <svg class="w-4 h-4 text-sky-400" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm4.64 6.8c-.15 1.58-.8 5.42-1.13 7.19-.14.75-.42 1-.68 1.03-.58.05-1.02-.38-1.58-.75-.88-.58-1.38-.94-2.23-1.5-.99-.65-.35-1.01.22-1.59.15-.15 2.71-2.48 2.76-2.69a.2.2 0 00-.05-.18c-.06-.05-.14-.03-.21-.02-.09.02-1.49.95-4.22 2.79-.4.27-.76.41-1.08.4-.36-.01-1.04-.2-1.55-.37-.63-.2-1.12-.31-1.08-.66.02-.18.27-.36.74-.55 2.92-1.27 4.86-2.11 5.83-2.51 2.78-1.16 3.35-1.36 3.73-1.36.08 0 .27.02.39.12.1.08.13.19.14.27-.01.06.01.24 0 .38z"/></svg>
                                <span>Telegram</span>
                            </a>
                            <a href="https://wa.me/78126042009" target="_blank" rel="noopener" class="btn-spring px-4 py-2 rounded-xl bg-white/10 hover:bg-white/20 text-white text-xs font-mono flex items-center space-x-2 border border-white/15">
                                <svg class="w-4 h-4 text-emerald-400" fill="currentColor" viewBox="0 0 24 24"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0012.04 2zm0 18.04c-1.49 0-2.95-.4-4.23-1.16l-.3-.18-3.14.82.84-3.06-.2-.31c-.83-1.33-1.27-2.88-1.27-4.47 0-4.47 3.64-8.11 8.12-8.11 2.17 0 4.21.85 5.74 2.38s2.38 3.57 2.38 5.74c0 4.47-3.64 8.11-8.12 8.11zm4.45-6.08c-.24-.12-1.45-.71-1.68-.79-.23-.09-.39-.12-.56.12-.17.24-.65.79-.8 1.03-.15.24-.3.27-.55.15-.24-.12-1.03-.38-1.96-1.21-.72-.65-1.21-1.45-1.35-1.69-.15-.24-.02-.37.1-.49.11-.11.24-.28.37-.43.12-.14.17-.24.25-.4.08-.17.04-.31-.02-.43-.06-.12-.56-1.35-.77-1.85-.2-.49-.41-.42-.56-.43h-.48c-.17 0-.44.06-.67.31-.23.24-.88.86-.88 2.1s.9 2.44 1.03 2.61c.12.17 1.77 2.7 4.29 3.79.6.26 1.07.41 1.43.53.6.19 1.15.16 1.58.1.48-.07 1.45-.59 1.66-1.16.2-.57.2-1.06.14-1.16-.06-.1-.23-.16-.47-.28z"/></svg>
                                <span>WhatsApp</span>
                            </a>
                        </div>
                    </div>
                </div>

                <!-- Right: Interactive Booking Form -->
                <div class="lg:col-span-6 bg-nordic-900 rounded-3xl p-8 sm:p-10 border border-white/10 shadow-2xl">
                    <h3 class="font-serif text-2xl sm:text-3xl font-bold text-white mb-2">Забронировать дату трансфера</h3>
                    <p class="text-stone-400 text-xs font-mono mb-6">Менеджер свяжется с вами в течение 10 минут для согласования времени.</p>

                    <form onsubmit="handleFormSubmit(event, 'VIP Transfer')" class="space-y-4">
                        <div>
                            <label class="block text-xs font-mono uppercase tracking-wider text-stone-300 mb-2">Ваше имя:</label>
                            <input type="text" required placeholder="Константин" class="w-full px-4 py-3 rounded-xl bg-white/5 border border-white/10 text-white placeholder-stone-500 focus:outline-none focus:border-brass-400 font-sans text-sm transition-colors">
                        </div>

                        <div>
                            <label class="block text-xs font-mono uppercase tracking-wider text-stone-300 mb-2">Номер телефона:</label>
                            <input type="tel" required placeholder="+7 (999) 000-00-00" class="w-full px-4 py-3 rounded-xl bg-white/5 border border-white/10 text-white placeholder-stone-500 focus:outline-none focus:border-brass-400 font-sans text-sm transition-colors">
                        </div>

                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                            <div>
                                <label class="block text-xs font-mono uppercase tracking-wider text-stone-300 mb-2">Выберите посёлок:</label>
                                <select class="w-full px-4 py-3 rounded-xl bg-nordic-800 border border-white/10 text-white focus:outline-none focus:border-brass-400 font-sans text-sm transition-colors">
                                    <option value="honkaniemi">Honkaniemi (Выборгский р-н)</option>
                                    <option value="sawoda">Sawoda (Тосненский р-н)</option>
                                    <option value="hytte">HYTTE (Всеволожский р-н)</option>
                                    <option value="yurki">Юрки (Кингисеппский р-н)</option>
                                    <option value="all">Все 4 посёлка (тур выходного дня)</option>
                                </select>
                            </div>

                            <div>
                                <label class="block text-xs font-mono uppercase tracking-wider text-stone-300 mb-2">Тип трансфера:</label>
                                <select class="w-full px-4 py-3 rounded-xl bg-nordic-800 border border-white/10 text-white focus:outline-none focus:border-brass-400 font-sans text-sm transition-colors">
                                    <option value="mercedes">Трансфер Mercedes / Genesis</option>
                                    <option value="self">Приеду на своём автомобиле</option>
                                </select>
                            </div>
                        </div>

                        <div class="pt-2">
                            <button type="submit" class="btn-spring w-full py-4 rounded-xl bg-brass-500 hover:bg-brass-400 text-nordic-950 font-semibold text-xs tracking-wider uppercase text-center shadow-glow-brass flex items-center justify-center space-x-2">
                                <span>Подтвердить запись на трансфер</span>
                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
                            </button>
                        </div>

                        <p class="text-[10px] text-stone-500 font-mono text-center">
                            Нажимая кнопку, вы соглашаетесь на обработку персональных данных в соответствии с 152-ФЗ.
                        </p>
                    </form>
                </div>
            </div>
        </div>
    </section>

    <!-- Refined Architectural Footer -->
    <footer class="bg-nordic-950 text-stone-400 py-16 border-t border-white/10 text-xs font-mono">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-1 md:grid-cols-4 gap-10 mb-12">
                <!-- Col 1: Brand & Atelier -->
                <div class="md:col-span-1">
                    <div class="flex items-center space-x-3 mb-4">
                        <div class="w-8 h-8 rounded-full bg-forest-900 border border-brass-500/40 flex items-center justify-center text-brass-400 font-serif font-bold">
                            М
                        </div>
                        <span class="font-serif tracking-widest text-base font-bold text-white uppercase">АТС МАЛИНОВКА</span>
                    </div>
                    <p class="text-stone-400 text-xs leading-relaxed mb-4 font-sans">
                        Архитектурный девелопмент загородных резиденций в Ленинградской области с 2009 года.
                    </p>
                    <div class="text-[11px] text-stone-500">
                        ОГРН 1144703002130 · ИНН 4703138870
                    </div>
                </div>

                <!-- Col 2: Settlements -->
                <div>
                    <div class="text-white uppercase font-bold tracking-wider mb-4 font-mono text-xs">Посёлки</div>
                    <ul class="space-y-2.5">
                        <li><a href="#villages" class="hover:text-brass-300 transition-colors">Honkaniemi (Выборгский)</a></li>
                        <li><a href="#villages" class="hover:text-brass-300 transition-colors">Sawoda (Тосненский)</a></li>
                        <li><a href="#villages" class="hover:text-brass-300 transition-colors">HYTTE (Всеволожский)</a></li>
                        <li><a href="#villages" class="hover:text-brass-300 transition-colors">Юрки (Кингисеппский)</a></li>
                        <li><a href="#villages" class="hover:text-brass-300 transition-colors">Scandi Barn 124</a></li>
                    </ul>
                </div>

                <!-- Col 3: Programs & Banking -->
                <div>
                    <div class="text-white uppercase font-bold tracking-wider mb-4 font-mono text-xs">Ипотечные программы</div>
                    <ul class="space-y-2.5">
                        <li><a href="#calculator" class="hover:text-brass-300 transition-colors">Семейная ипотека 6%</a></li>
                        <li><a href="#calculator" class="hover:text-brass-300 transition-colors">IT-ипотека в ЛО 6%</a></li>
                        <li><a href="#calculator" class="hover:text-brass-300 transition-colors">Синхронный Trade-In</a></li>
                        <li><a href="#calculator" class="hover:text-brass-300 transition-colors">Банки-партнеры</a></li>
                        <li><a href="#standards" class="hover:text-brass-300 transition-colors">Собственный капитал</a></li>
                    </ul>
                </div>

                <!-- Col 4: Contacts & Office -->
                <div>
                    <div class="text-white uppercase font-bold tracking-wider mb-4 font-mono text-xs">Контакты</div>
                    <div class="space-y-2.5 text-stone-300">
                        <div>
                            <a href="tel:+78126042009" class="text-white font-mono text-sm hover:text-brass-300 transition-colors font-bold">+7 (812) 604-20-09</a>
                        </div>
                        <div class="text-xs">Ежедневно с 09:00 до 21:00</div>
                        <div class="text-xs text-stone-400">Санкт-Петербург, Выборгское шоссе / Шоу-рум в посёлках</div>
                    </div>
                </div>
            </div>

            <!-- Bottom Copyright & Legal -->
            <div class="pt-8 border-t border-white/10 flex flex-col sm:flex-row items-center justify-between text-stone-500 text-[11px]">
                <div>© 2009–2026 Девелоперская компания «АТС Малиновка». Все права защищены.</div>
                <div class="mt-4 sm:mt-0 flex items-center space-x-6">
                    <a href="#" class="hover:text-stone-300 transition-colors">Политика конфиденциальности</a>
                    <a href="#" class="hover:text-stone-300 transition-colors">Пользовательское соглашение</a>
                </div>
            </div>
        </div>
    </footer>
    '''

def get_modal_and_toast():
    return '''
    <!-- Mobile Sticky Quick Action Bar -->
    <div class="md:hidden fixed bottom-4 inset-x-4 z-40">
        <div class="glass-panel-dark rounded-2xl p-2 border border-white/15 shadow-2xl flex items-center gap-2">
            <a href="tel:+78126042009" class="btn-spring flex-1 py-3 px-3 rounded-xl bg-white/10 text-white font-mono text-xs uppercase tracking-wider text-center flex items-center justify-center space-x-1.5 border border-white/10">
                <svg class="w-3.5 h-3.5 text-brass-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
                <span>Позвонить</span>
            </a>
            <button onclick="openModal('vipModal')" class="btn-spring flex-1 py-3 px-3 rounded-xl bg-brass-500 text-nordic-950 font-mono text-xs uppercase tracking-wider text-center font-bold shadow-glow-brass flex items-center justify-center space-x-1.5">
                <span>VIP Трансфер</span>
            </button>
        </div>
    </div>

    <!-- Universal Modal System -->
    <!-- Modal 1: Catalog & Plans Download -->
    <div id="catalogModal" class="modal-overlay fixed inset-0 z-50 bg-black/80 backdrop-blur-md hidden items-center justify-center p-4">
        <div class="modal-content relative w-full max-w-lg bg-nordic-900 border border-white/15 rounded-3xl p-6 sm:p-8 text-white shadow-2xl transition-all duration-300">
            <button onclick="closeModal('catalogModal')" class="absolute top-5 right-5 text-stone-400 hover:text-white p-2 rounded-full bg-white/5 hover:bg-white/10 transition-colors">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
            </button>
            <div class="mb-6">
                <span class="px-3 py-1 rounded-full text-[10px] font-mono uppercase tracking-wider bg-brass-500/20 text-brass-300 border border-brass-500/40">Каталог 2026 · PDF 28 МБ</span>
                <h3 class="font-serif text-2xl sm:text-3xl font-bold mt-3 mb-2">Получить полный каталог посёлков и планировок</h3>
                <p class="text-stone-300 text-xs sm:text-sm font-light">Отправим файл в Telegram или WhatsApp вместе с актуальным генпланом свободных участков.</p>
            </div>
            <form onsubmit="handleFormSubmit(event, 'Каталог PDF')" class="space-y-4">
                <div>
                    <label class="block text-xs font-mono uppercase tracking-wider text-stone-300 mb-1.5">Ваше имя:</label>
                    <input type="text" required placeholder="Александр" class="w-full px-4 py-3 rounded-xl bg-white/5 border border-white/10 text-white placeholder-stone-500 focus:outline-none focus:border-brass-400 font-sans text-sm">
                </div>
                <div>
                    <label class="block text-xs font-mono uppercase tracking-wider text-stone-300 mb-1.5">Номер телефона:</label>
                    <input type="tel" required placeholder="+7 (999) 000-00-00" class="w-full px-4 py-3 rounded-xl bg-white/5 border border-white/10 text-white placeholder-stone-500 focus:outline-none focus:border-brass-400 font-sans text-sm">
                </div>
                <div>
                    <label class="block text-xs font-mono uppercase tracking-wider text-stone-300 mb-1.5">Куда отправить каталог:</label>
                    <div class="grid grid-cols-2 gap-3">
                        <label class="flex items-center space-x-2 p-3 rounded-xl bg-white/5 border border-white/10 cursor-pointer hover:border-brass-400/60 transition-colors">
                            <input type="radio" name="messenger" value="telegram" checked class="text-brass-500 focus:ring-0">
                            <span class="text-xs font-mono text-stone-200">Telegram</span>
                        </label>
                        <label class="flex items-center space-x-2 p-3 rounded-xl bg-white/5 border border-white/10 cursor-pointer hover:border-brass-400/60 transition-colors">
                            <input type="radio" name="messenger" value="whatsapp" class="text-brass-500 focus:ring-0">
                            <span class="text-xs font-mono text-stone-200">WhatsApp</span>
                        </label>
                    </div>
                </div>
                <button type="submit" class="btn-spring w-full py-4 rounded-xl bg-brass-500 hover:bg-brass-400 text-nordic-950 font-semibold text-xs tracking-wider uppercase text-center shadow-glow-brass mt-2">
                    Скачать каталог и генпланы
                </button>
            </form>
        </div>
    </div>

    <!-- Modal 2: VIP Test Drive Modal -->
    <div id="vipModal" class="modal-overlay fixed inset-0 z-50 bg-black/80 backdrop-blur-md hidden items-center justify-center p-4">
        <div class="modal-content relative w-full max-w-lg bg-nordic-900 border border-white/15 rounded-3xl p-6 sm:p-8 text-white shadow-2xl transition-all duration-300">
            <button onclick="closeModal('vipModal')" class="absolute top-5 right-5 text-stone-400 hover:text-white p-2 rounded-full bg-white/5 hover:bg-white/10 transition-colors">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
            </button>
            <div class="mb-6">
                <span class="px-3 py-1 rounded-full text-[10px] font-mono uppercase tracking-wider bg-brass-500/20 text-brass-300 border border-brass-500/40">Персональный тур</span>
                <h3 class="font-serif text-2xl sm:text-3xl font-bold mt-3 mb-2">Заказ VIP-трансфера в посёлки</h3>
                <p class="text-stone-300 text-xs sm:text-sm font-light">Бесплатный автомобиль бизнес-класса туда и обратно. Личный архитектор-гид.</p>
            </div>
            <form onsubmit="handleFormSubmit(event, 'VIP Трансфер Модал')" class="space-y-4">
                <div>
                    <label class="block text-xs font-mono uppercase tracking-wider text-stone-300 mb-1.5">Ваше имя:</label>
                    <input type="text" required placeholder="Дмитрий" class="w-full px-4 py-3 rounded-xl bg-white/5 border border-white/10 text-white placeholder-stone-500 focus:outline-none focus:border-brass-400 font-sans text-sm">
                </div>
                <div>
                    <label class="block text-xs font-mono uppercase tracking-wider text-stone-300 mb-1.5">Телефон для связи:</label>
                    <input type="tel" required placeholder="+7 (999) 000-00-00" class="w-full px-4 py-3 rounded-xl bg-white/5 border border-white/10 text-white placeholder-stone-500 focus:outline-none focus:border-brass-400 font-sans text-sm">
                </div>
                <div>
                    <label class="block text-xs font-mono uppercase tracking-wider text-stone-300 mb-1.5">Локация для визита:</label>
                    <select class="w-full px-4 py-3 rounded-xl bg-nordic-800 border border-white/10 text-white font-sans text-sm focus:outline-none focus:border-brass-400">
                        <option>Honkaniemi (Выборгский р-н)</option>
                        <option>Sawoda (Тосненский р-н)</option>
                        <option>HYTTE (Всеволожский р-н)</option>
                        <option>Юрки (Кингисеппский р-н)</option>
                    </select>
                </div>
                <button type="submit" class="btn-spring w-full py-4 rounded-xl bg-brass-500 hover:bg-brass-400 text-nordic-950 font-semibold text-xs tracking-wider uppercase text-center shadow-glow-brass mt-2">
                    Заказать бесплатный трансфер
                </button>
            </form>
        </div>
    </div>

    <!-- Modal 3: Mortgage Pre-Approval Modal -->
    <div id="calcLeadModal" class="modal-overlay fixed inset-0 z-50 bg-black/80 backdrop-blur-md hidden items-center justify-center p-4">
        <div class="modal-content relative w-full max-w-lg bg-nordic-900 border border-white/15 rounded-3xl p-6 sm:p-8 text-white shadow-2xl transition-all duration-300">
            <button onclick="closeModal('calcLeadModal')" class="absolute top-5 right-5 text-stone-400 hover:text-white p-2 rounded-full bg-white/5 hover:bg-white/10 transition-colors">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
            </button>
            <div class="mb-6">
                <span class="px-3 py-1 rounded-full text-[10px] font-mono uppercase tracking-wider bg-emerald-500/20 text-emerald-300 border border-emerald-500/40">Ипотека 6%</span>
                <h3 class="font-serif text-2xl sm:text-3xl font-bold mt-3 mb-2">Одобрение ипотеки за 24 часа</h3>
                <p class="text-stone-300 text-xs sm:text-sm font-light">Подадим заявку сразу в 12 аккредитованных банков-партнёров по одной анкете без очередей.</p>
            </div>
            <form onsubmit="handleFormSubmit(event, 'Одобрение ипотеки')" class="space-y-4">
                <div>
                    <label class="block text-xs font-mono uppercase tracking-wider text-stone-300 mb-1.5">Ваше имя:</label>
                    <input type="text" required placeholder="Елена" class="w-full px-4 py-3 rounded-xl bg-white/5 border border-white/10 text-white placeholder-stone-500 focus:outline-none focus:border-brass-400 font-sans text-sm">
                </div>
                <div>
                    <label class="block text-xs font-mono uppercase tracking-wider text-stone-300 mb-1.5">Номер телефона:</label>
                    <input type="tel" required placeholder="+7 (999) 000-00-00" class="w-full px-4 py-3 rounded-xl bg-white/5 border border-white/10 text-white placeholder-stone-500 focus:outline-none focus:border-brass-400 font-sans text-sm">
                </div>
                <button type="submit" class="btn-spring w-full py-4 rounded-xl bg-brass-500 hover:bg-brass-400 text-nordic-950 font-semibold text-xs tracking-wider uppercase text-center shadow-glow-brass mt-2">
                    Получить одобрение по ставке 6%
                </button>
            </form>
        </div>
    </div>

    <!-- Modal 4: Project Details / Floorplans Modal -->
    <div id="projectModal" class="modal-overlay fixed inset-0 z-50 bg-black/80 backdrop-blur-md hidden items-center justify-center p-4">
        <div class="modal-content relative w-full max-w-2xl bg-nordic-900 border border-white/15 rounded-3xl p-6 sm:p-8 text-white shadow-2xl transition-all duration-300 max-h-[90vh] overflow-y-auto">
            <button onclick="closeModal('projectModal')" class="absolute top-5 right-5 text-stone-400 hover:text-white p-2 rounded-full bg-white/5 hover:bg-white/10 transition-colors z-10">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
            </button>
            <div class="h-64 sm:h-72 rounded-2xl overflow-hidden mb-6 relative">
                <img id="projModalImg" src="" alt="Project" class="w-full h-full object-cover">
                <div class="absolute inset-0 bg-gradient-to-t from-nordic-950/80 via-transparent to-transparent"></div>
                <div class="absolute bottom-4 left-4 right-4">
                    <span id="projModalLoc" class="text-xs font-mono text-brass-300 uppercase">Локация</span>
                    <h3 id="projModalTitle" class="font-serif text-2xl sm:text-3xl font-bold text-white">Название проекта</h3>
                </div>
            </div>
            <div class="flex items-center justify-between pb-4 border-b border-white/10 mb-4">
                <span class="text-xs font-mono uppercase tracking-wider text-stone-400">Стоимость под ключ с участком:</span>
                <span id="projModalPrice" class="font-serif text-2xl font-bold text-brass-300">от 0 ₽</span>
            </div>
            <p id="projModalDesc" class="text-stone-300 text-sm leading-relaxed mb-6 font-light">
                Описание проекта...
            </p>
            <div class="flex flex-col sm:flex-row gap-3">
                <button onclick="closeModal('projectModal'); openModal('catalogModal');" class="btn-spring flex-1 py-3.5 px-4 rounded-xl bg-brass-500 hover:bg-brass-400 text-nordic-950 font-semibold text-xs tracking-wider uppercase text-center shadow-glow-brass">
                    Получить архитектурный альбом (PDF)
                </button>
                <button onclick="closeModal('projectModal'); openModal('vipModal');" class="btn-spring flex-1 py-3.5 px-4 rounded-xl bg-white/10 hover:bg-white/20 text-white font-mono text-xs uppercase tracking-wider text-center border border-white/15">
                    Записаться на просмотр
                </button>
            </div>
        </div>
    </div>

    <!-- Toast Feedback Notification -->
    <div id="toastAlert" class="fixed top-6 right-6 z-50 transform translate-y-[-120%] opacity-0 transition-all duration-300 pointer-events-none">
        <div class="glass-panel-dark px-5 py-3.5 rounded-2xl border border-brass-400/50 shadow-2xl flex items-center space-x-3 text-white">
            <div class="w-6 h-6 rounded-full bg-emerald-500/20 text-emerald-400 flex items-center justify-center font-bold text-xs">✓</div>
            <div>
                <div class="text-xs font-mono font-bold text-white">Заявка принята!</div>
                <div class="text-[11px] text-stone-300" id="toastMessage">Менеджер свяжется с вами в течение 10 минут.</div>
            </div>
        </div>
    </div>
    '''

def get_scripts():
    return '''
    <!-- Interactive Client Engine -->
    <script>
        // 1. Hero Dynamic Village Switcher
        const heroVillages = [
            { id: 0, coords: "60°18'N 29°52'E · Карельский перешеек", bg: "assets/honkaniemi-forest.jpg" },
            { id: 1, coords: "59°28'N 31°12'E · Тосненский район", bg: "assets/sawoda-facade-new.png" },
            { id: 2, coords: "59°58'N 30°38'E · Всеволожский район (25 мин до КАД)", bg: "assets/hytte-house.jpg" },
            { id: 3, coords: "59°22'N 28°36'E · Кингисеппский район (р. Луга)", bg: "assets/yurki-cottage.jpg" }
        ];

        function switchHeroVillage(index) {
            // Update tabs active state
            document.querySelectorAll('.hero-village-tab').forEach((tab, i) => {
                if (i === index) {
                    tab.classList.add('active', 'bg-white/15', 'border-brass-400/80');
                    tab.classList.remove('bg-white/5', 'border-white/10');
                } else {
                    tab.classList.remove('active', 'bg-white/15', 'border-brass-400/80');
                    tab.classList.add('bg-white/5', 'border-white/10');
                }
            });

            // Update backgrounds with smooth cross-fade
            document.querySelectorAll('.hero-bg').forEach((img, i) => {
                if (i === index) {
                    img.classList.remove('opacity-0', 'pointer-events-none');
                    img.classList.add('opacity-100');
                } else {
                    img.classList.remove('opacity-100');
                    img.classList.add('opacity-0', 'pointer-events-none');
                }
            });

            // Update coordinates label
            const coordsEl = document.getElementById('heroCoordinates');
            if (coordsEl) {
                coordsEl.textContent = heroVillages[index].coords;
            }
        }

        // 2. Catalog Category Filter
        function filterCatalog(category) {
            // Update buttons
            document.querySelectorAll('.catalog-filter-btn').forEach(btn => {
                btn.classList.remove('active', 'bg-forest-900', 'text-white', 'shadow-sm');
                btn.classList.add('text-stone-600');
            });
            event.currentTarget.classList.add('active', 'bg-forest-900', 'text-white', 'shadow-sm');
            event.currentTarget.classList.remove('text-stone-600');

            // Filter cards
            document.querySelectorAll('.catalog-card').forEach(card => {
                if (category === 'all' || card.dataset.category === category) {
                    card.style.display = 'block';
                } else {
                    card.style.display = 'none';
                }
            });
        }

        // 3. Project Detail Modal Opener
        function openProjectModal(title, location, price, img, desc) {
            document.getElementById('projModalTitle').innerText = title;
            document.getElementById('projModalLoc').innerText = location;
            document.getElementById('projModalPrice').innerText = price;
            document.getElementById('projModalImg').src = img;
            document.getElementById('projModalDesc').innerText = desc;
            openModal('projectModal');
        }

        // 4. Smooth FAQ Accordion
        document.querySelectorAll('.accordion-toggle').forEach(button => {
            button.addEventListener('click', () => {
                const item = button.closest('.accordion-item');
                const wasOpen = item.classList.contains('open');
                document.querySelectorAll('.accordion-item').forEach(i => i.classList.remove('open'));
                if (!wasOpen) {
                    item.classList.add('open');
                }
            });
        });
        const firstFaq = document.querySelector('.accordion-item');
        if (firstFaq) firstFaq.classList.add('open');

        // 5. Interactive Mortgage Calculator 2026 Engine
        const priceRange = document.getElementById('priceRange');
        const downRange = document.getElementById('downRange');
        const yearsRange = document.getElementById('yearsRange');
        const priceVal = document.getElementById('priceVal');
        const downVal = document.getElementById('downVal');
        const yearsVal = document.getElementById('yearsVal');
        const monthlyPayment = document.getElementById('monthlyPayment');
        const loanSum = document.getElementById('loanSum');
        const incomeNeeded = document.getElementById('incomeNeeded');
        const savingsVal = document.getElementById('savingsVal');
        const comboAlert = document.getElementById('comboAlert');
        const programDescription = document.getElementById('programDescription');

        let currentProgram = 'family';
        let currentRate = 6.0;
        let currentLimit = 12000000;

        const programConfigs = {
            family: {
                rate: 6.0,
                limit: 12000000,
                desc: '<strong class="text-nordic-900">Семейная ипотека 6%:</strong> Лимит субсидии в Ленинградской области до 12 000 000 ₽. Доступна семьям с ребенком в возрасте до 6 лет включительно. Первоначальный взнос от 20%.'
            },
            it: {
                rate: 6.0,
                limit: 9000000,
                desc: '<strong class="text-nordic-900">IT-ипотека 6% в ЛО:</strong> В Санкт-Петербурге и Москве программа закрыта, но в Ленинградской области действует! Лимит до 9 000 000 ₽. Для сотрудников аккредитованных IT-компаний. ПВ от 20%.'
            },
            base: {
                rate: 23.0,
                limit: 50000000,
                desc: '<strong class="text-nordic-900">Базовая рыночная ипотека 23%:</strong> Стандартная банковская программа без льгот (исходя из ключевой ставки ЦБ РФ 2026 года). Сумма кредита до 50 000 000 ₽, ПВ от 20%.'
            },
            tradein: {
                rate: 6.0,
                limit: 12000000,
                desc: '<strong class="text-nordic-900">Синхронный Trade-In + Льготная ипотека:</strong> Ваша городская квартира в Санкт-Петербурге засчитывается как первоначальный взнос (до 80% от цены дома), а остаток оформляется в льготную ипотеку под 6%.'
            }
        };

        function setProgram(prog) {
            currentProgram = prog;
            const cfg = programConfigs[prog];
            currentRate = cfg.rate;
            currentLimit = cfg.limit;

            // Update UI buttons
            document.querySelectorAll('.calc-prog-btn').forEach(btn => {
                btn.classList.remove('active', 'bg-forest-900', 'text-white', 'shadow-md');
                btn.classList.add('text-stone-700');
            });
            const activeBtn = document.getElementById('progBtn' + prog.charAt(0).toUpperCase() + prog.slice(1));
            if (activeBtn) {
                activeBtn.classList.add('active', 'bg-forest-900', 'text-white', 'shadow-md');
                activeBtn.classList.remove('text-stone-700');
            }

            // If tradein selected, set down payment to higher default
            if (prog === 'tradein') {
                downRange.value = 65;
            }

            programDescription.innerHTML = cfg.desc;
            calculateMortgage();
        }

        function formatNumber(num) {
            return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, " ");
        }

        function calculateAnnuity(loan, annualRate, months) {
            if (loan <= 0) return 0;
            const monthlyRate = (annualRate / 100) / 12;
            if (monthlyRate === 0) return loan / months;
            return loan * (monthlyRate * Math.pow(1 + monthlyRate, months)) / (Math.pow(1 + monthlyRate, months) - 1);
        }

        function calculateMortgage() {
            const price = parseInt(priceRange.value);
            const downPercent = parseInt(downRange.value);
            const years = parseInt(yearsRange.value);
            const months = years * 12;

            const downAmount = Math.round(price * (downPercent / 100));
            const loan = price - downAmount;

            priceVal.innerText = formatNumber(price) + ' ₽';
            downVal.innerText = formatNumber(downAmount) + ' ₽ (' + downPercent + '%)';
            yearsVal.innerText = years + ' лет';
            loanSum.innerText = formatNumber(loan) + ' ₽';

            let payment = 0;

            if (currentProgram === 'base' || loan <= currentLimit) {
                comboAlert.classList.add('hidden');
                payment = calculateAnnuity(loan, currentRate, months);
            } else {
                // Combo Mortgage: subsidized part up to limit + market rate (23%) on remainder
                comboAlert.classList.remove('hidden');
                const subsidizedLoan = currentLimit;
                const marketLoan = loan - currentLimit;
                const subsidizedPayment = calculateAnnuity(subsidizedLoan, currentRate, months);
                const marketPayment = calculateAnnuity(marketLoan, 23.0, months);
                payment = subsidizedPayment + marketPayment;
            }

            const paymentRound = Math.round(payment);
            monthlyPayment.innerText = formatNumber(paymentRound) + ' ₽';

            // Required income estimation
            const income = Math.round(paymentRound * 2.05 / 1000) * 1000;
            incomeNeeded.innerText = 'от ' + formatNumber(income) + ' ₽/мес';

            // Government subsidy savings compared to base 23%
            const marketTotal = calculateAnnuity(loan, 23.0, months) * months;
            const actualTotal = payment * months;
            const totalSavings = Math.max(0, Math.round((marketTotal - actualTotal) / 100000) * 100000);
            savingsVal.innerText = 'до ' + formatNumber(totalSavings) + ' ₽';
        }

        priceRange.addEventListener('input', calculateMortgage);
        downRange.addEventListener('input', calculateMortgage);
        yearsRange.addEventListener('input', calculateMortgage);

        // Initial calculation
        calculateMortgage();

        // 6. Universal Modal Controls
        function openModal(id) {
            const modal = document.getElementById(id);
            if (modal) {
                modal.classList.remove('hidden');
                modal.classList.add('flex');
                document.body.style.overflow = 'hidden';
            }
        }

        function closeModal(id) {
            const modal = document.getElementById(id);
            if (modal) {
                modal.classList.add('hidden');
                modal.classList.remove('flex');
                document.body.style.overflow = '';
            }
        }

        // Close on ESC key or clicking background
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                document.querySelectorAll('.modal-overlay').forEach(m => {
                    m.classList.add('hidden');
                    m.classList.remove('flex');
                });
                document.body.style.overflow = '';
            }
        });

        document.querySelectorAll('.modal-overlay').forEach(overlay => {
            overlay.addEventListener('click', (e) => {
                if (e.target === overlay) {
                    overlay.classList.add('hidden');
                    overlay.classList.remove('flex');
                    document.body.style.overflow = '';
                }
            });
        });

        // 7. Form Submit Handler with Toast Feedback
        function handleFormSubmit(event, formName) {
            event.preventDefault();
            // Close active modals
            document.querySelectorAll('.modal-overlay').forEach(m => {
                m.classList.add('hidden');
                m.classList.remove('flex');
            });
            document.body.style.overflow = '';

            // Show Toast Alert
            const toast = document.getElementById('toastAlert');
            const toastMsg = document.getElementById('toastMessage');
            if (toast) {
                toastMsg.innerText = 'Заявка («' + formName + '») успешно отправлена! Менеджер свяжется с вами в течение 10 минут.';
                toast.classList.remove('translate-y-[-120%]', 'opacity-0');
                toast.classList.add('translate-y-0', 'opacity-100');

                setTimeout(() => {
                    toast.classList.remove('translate-y-0', 'opacity-100');
                    toast.classList.add('translate-y-[-120%]', 'opacity-0');
                }, 4500);
            }

            // Reset the form
            event.target.reset();
        }
    </script>
</body>
</html>
    '''

def main():
    target_file = "/Users/murad/Downloads/Проект АТС Малиновка /landing/index.html"
    print("Assembling HTML parts...")
    parts = [
        get_head(),
        get_nav(),
        get_hero(),
        get_jtbd(),
        get_catalog(),
        get_manifesto(),
        get_calculator(),
        get_comparison_matrix(),
        get_faq(),
        get_about(),
        get_contact(),
        get_modal_and_toast(),
        get_scripts()
    ]
    full_html = "".join(parts)
    print("Writing to:", target_file)
    with open(target_file, "w", encoding="utf-8") as f:
        f.write(full_html)
    
    file_size = os.path.getsize(target_file)
    print(f"SUCCESS! {target_file} written successfully.")
    print(f"File size: {file_size / 1024:.2f} KB ({file_size} bytes)")

if __name__ == "__main__":
    main()
