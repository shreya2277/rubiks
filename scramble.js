import { makeAutoMove } from './action_utils.js';
import { disableManualButtons } from './ui.js';
import { isAutoSolveMode } from './modes.js';

// Valid moves for scrambling
const VALID_MOVES = ["R", "R'", "L", "L'", "U", "U'", "D", "D'", "F", "F'", "B", "B'"];

// Global flag to prevent interaction during scrambling
let isScrambling = false;

// Generate a random move from the valid moves array
function getRandomMove() {
    return VALID_MOVES[Math.floor(Math.random() * VALID_MOVES.length)];
}

// Generate a scramble sequence of 20 moves
function generateScrambleSequence() {
    const sequence = [];
    let lastMove = '';
    let secondLastMove = '';
    
    for (let i = 0; i < 20; i++) {
        let move;
        do {
            move = getRandomMove();
        } while (
            // Avoid repeating the same move
            move === lastMove ||
            // Avoid doing opposite moves on the same face (e.g., R followed by R')
            (move.charAt(0) === lastMove.charAt(0) && move !== lastMove) ||
            // Avoid doing the same move three times in a row
            (move === lastMove && move === secondLastMove)
        );
        
        sequence.push(move);
        secondLastMove = lastMove;
        lastMove = move;
    }
    
    return sequence;
}

// Apply moves one by one with delay
async function applyScrambleSequence(sequence) {
    isScrambling = true;
    disableManualButtons(true);
    
    try {
        for (let i = 0; i < sequence.length; i++) {
            const move = sequence[i];
            
            // Apply the move
            await makeAutoMove(move, true);
            
            // Wait before next move (300ms delay)
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

// Main scramble function
async function scrambleCube() {
    console.log("scrambleCube function called!"); // Debug log
    
    // Prevent scrambling if already in progress or in auto-solve mode
    if (isScrambling || isAutoSolveMode()) {
        console.log("Scrambling blocked: already scrambling or in auto-solve mode");
        return;
    }
    
    console.log("Starting cube scramble...");
    
    // Generate scramble sequence
    const scrambleSequence = generateScrambleSequence();
    console.log("Scramble sequence:", scrambleSequence.join(' '));
    
    // Apply the sequence
    await applyScrambleSequence(scrambleSequence);
    
    console.log("Cube scramble completed!");
}

// Export the flag for other modules to check
export function getIsScrambling() {
    return isScrambling;
}

// Make scrambleCube available globally - try multiple approaches
window.scrambleCube = scrambleCube;

// Also try setting it after a short delay
setTimeout(() => {
    window.scrambleCube = scrambleCube;
    console.log("Delayed assignment - window.scrambleCube:", typeof window.scrambleCube);
}, 100);

// Debug: Check if function is properly exposed
console.log("Scramble module loaded, window.scrambleCube:", typeof window.scrambleCube); 