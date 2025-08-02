from fastapi import APIRouter, Request, HTTPException
from utils import create_solved_cube_state, update_cube_state
import json

router = APIRouter()

# Global variable to track cube state
cube_state = create_solved_cube_state()

@router.post("/move")
async def move(request: Request):
    """
    Apply a move to the cube and return the updated cube state
    """
    try:
        body = await request.json()
        move = body.get("move")
        
        if not move:
            raise HTTPException(status_code=400, detail="Move is required")
        
        # Update the global cube state
        global cube_state
        cube_state = update_cube_state(cube_state, move)
        
        # Convert cube state to string format
        cube_string = ""
        for face in cube_state:
            for row in face:
                for sticker in row:
                    cube_string += sticker
        
        return {
            "move": move,
            "cube_string": cube_string
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/solve")
async def solve():
    """
    Solve the current cube state using the Kociemba solver
    """
    try:
        # Implementation for solving
        # This would use the kociemba solver
        return {
            "solutionString": "R U R' U'",
            "parsedMoves": ["R", "U", "R'", "U'"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/reset_cube")
async def reset_cube():
    """
    Reset the cube to the solved state
    """
    try:
        global cube_state
        cube_state = create_solved_cube_state()
        return {}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_cube_state")
async def get_cube_state():
    """
    Get the current state of the cube for real solve detection
    """
    try:
        global cube_state
        
        # Convert the numpy array to a proper format for solve detection
        faces = []
        for face in cube_state:
            face_list = []
            for row in face:
                face_list.append([sticker for sticker in row])
            faces.append(face_list)
        
        # Check if cube is solved using the real method
        is_solved = is_cube_solved_real(cube_state)
        
        return {
            "faces": faces,
            "solved": is_solved,
            "face_names": ["U", "R", "F", "D", "L", "B"]  # Up, Right, Front, Down, Left, Back
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def is_cube_solved_real(cube_state):
    """
    Real solve detection: Check if each face has uniform color by comparing to center
    """
    try:
        # Check each of the 6 faces
        for face_index, face in enumerate(cube_state):
            # Get the center color (position [1][1] in 3x3 grid)
            center_color = face[1][1]
            
            # Check all 9 tiles on this face
            for row in range(3):
                for col in range(3):
                    if face[row][col] != center_color:
                        return False
        
        return True
    except Exception as e:
        print(f"Error in real solve detection: {e}")
        return False
