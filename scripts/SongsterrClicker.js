// ==UserScript==
// @name         Songsterr Auto Clicker
// @version      1.0
// @description  Auto clicks Songsterr popups.
// @author       OPGman
// @grant        none
// @match        https://*.songsterr.com/*
// ==/UserScript==

( function() {
    'use strict';
    function clicker() {
        let list = document.querySelectorAll( "a" );
        for ( let a of list ) {
            if ( a.href == window.location.href ) {
                a.click();
                break;
            }
        }
    }
    setInterval( clicker, 350 );
} )();
