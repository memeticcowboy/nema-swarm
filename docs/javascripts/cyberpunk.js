/**
 * NEMA SWARM — Cyberpunk Theme JavaScript
 * Handles element-specific page theming and effects
 */

(function() {
  'use strict';

  // Element detection from URL path
  const ELEMENT_MAP = {
    'aether': 'element-aether',
    'air': 'element-air',
    'water': 'element-water',
    'fire': 'element-fire',
    'wood': 'element-wood',
    'earth': 'element-earth',
    'metal': 'element-metal'
  };

  function applyElementTheme() {
    var path = window.location.pathname.toLowerCase();
    var content = document.querySelector('.md-content');
    if (!content) return;

    // Remove any existing element classes
    content.className = content.className.replace(/element-\w+/g, '').trim();
    content.className = content.className.replace(/siml-terminal/g, '').trim();

    // Check for SIML pages
    if (path.indexOf('/siml/') !== -1) {
      content.classList.add('siml-terminal');
      return;
    }

    // Check for element pages
    for (var element in ELEMENT_MAP) {
      if (path.indexOf('/elements/' + element) !== -1 ||
          path.indexOf('/' + element + '/') !== -1 ||
          path.indexOf('/' + element + '.') !== -1) {
        content.classList.add(ELEMENT_MAP[element]);
        return;
      }
    }

    // Default: aether theme for homepage and general pages
    if (path === '/' || path === '/index.html' || path === '') {
      content.classList.add('element-aether');
    }
  }

  // Apply on page load
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', applyElementTheme);
  } else {
    applyElementTheme();
  }

  // Re-apply on navigation (MkDocs Material uses instant loading)
  if (typeof document$ !== 'undefined') {
    document$.subscribe(function() {
      applyElementTheme();
    });
  } else {
    // Fallback: watch for URL changes
    var lastPath = window.location.pathname;
    setInterval(function() {
      if (window.location.pathname !== lastPath) {
        lastPath = window.location.pathname;
        applyElementTheme();
      }
    }, 200);
  }
})();
