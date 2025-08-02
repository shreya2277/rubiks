import './modes.js'; // defines the different operational modes of the app
import {initMotions, updateAnimations} from './animations.js'; // defines face rotation animations
import {initCanvas} from './sceneManager.js'; // sets up the canvas and asynchronously renders the scene using an update callback
import { resetCubeObject} from './rubik.js'; // defines the cube and its actions
import './action_utils.js'; // manages user interactions, performs moves, and displays action info on the GUI
import { initKeyHandler } from './keyHandler.js';
import './solutionService.js'; // implements functions for autosolve mode
import './scramble.js'; // implements scramble functionality
import { render } from './sceneManager.js';
import { resetMode } from './modes.js';
import { resetBackendState } from './api.js';
import { clearAllDisplays } from './ui.js';
import { makeAutoMove } from './action_utils.js';
import { disableManualButtons } from './ui.js';
import { isAutoSolveMode } from './modes.js';


initCanvas();
resetState();

// update callback
async function update() {
    updateAnimations();
    requestAnimationFrame(update); // requests the next update call; this creates a loop
    render();
}
update();

export function resetState() {
    resetBackendState();
    sessionStorage.clear();
    resetCubeObject();
    initMotions(true);
    initKeyHandler();
    resetMode();
    clearAllDisplays();
}
window.resetState = resetState;

// Alternative scramble function directly in main.js
const VALID_MOVES = ["R", "R'", "L", "L'", "U", "U'", "D", "D'", "F", "F'", "B", "B'"];
let isScrambling = false;

function getRandomMove() {
    return VALID_MOVES[Math.floor(Math.random() * VALID_MOVES.length)];
}

function generateScrambleSequence() {
    const sequence = [];
    let lastMove = '';
    let secondLastMove = '';
    
    for (let i = 0; i < 20; i++) {
        let move;
        do {
            move = getRandomMove();
        } while (
            move === lastMove ||
            (move.charAt(0) === lastMove.charAt(0) && move !== lastMove) ||
            (move === lastMove && move === secondLastMove)
        );
        
        sequence.push(move);
        secondLastMove = lastMove;
        lastMove = move;
    }
    
    return sequence;
}

async function applyScrambleSequence(sequence) {
    isScrambling = true;
    disableManualButtons(true);
    
    try {
        for (let i = 0; i < sequence.length; i++) {
            const move = sequence[i];
            await makeAutoMove(move, true);
            if (i < sequence.length - 1) {
                await new Promise(resolve => setTimeout(resolve, 300));
            }
        }
    } catch (error) {
        console.error("Error during scrambling:", error);
    } finally {
        isScrambling = false;
        disableManualButtons(false);
    }
}

async function scrambleCube() {
    console.log("scrambleCube function called from main.js!");
    
    if (isScrambling || isAutoSolveMode()) {
        console.log("Scrambling blocked: already scrambling or in auto-solve mode");
        return;
    }
    
    console.log("Starting cube scramble...");
    
    const scrambleSequence = generateScrambleSequence();
    console.log("Scramble sequence:", scrambleSequence.join(' '));
    
    await applyScrambleSequence(scrambleSequence);
    
    console.log("Cube scramble completed!");
}

// Make scrambleCube available globally
window.scrambleCube = scrambleCube;