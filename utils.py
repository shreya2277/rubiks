import numpy as np


def create_solved_cube_state():
    return np.array(
        [
            [["U"] * 3 for _ in range(3)],  # white
            [["R"] * 3 for _ in range(3)],  # blue
            [["F"] * 3 for _ in range(3)],  # red
            [["D"] * 3 for _ in range(3)],  # yellow
            [["L"] * 3 for _ in range(3)],  # green
            [["B"] * 3 for _ in range(3)],  # orange
        ]
    )


def rotate_face_clockwise(face):
    return np.rot90(face, -1)


def rotate_face_counterclockwise(face):
    return np.rot90(face, 1)


# rotation direction wrt to looking at the face
def rotate_cube_face(cube_state: np.array, face_idx: int, clockwise=True):
    if clockwise:
        cube_state[face_idx] = rotate_face_clockwise(cube_state[face_idx])
    else:
        cube_state[face_idx] = rotate_face_counterclockwise(cube_state[face_idx])


# Rotate F clockwise
def rotate_front_clockwise(cube_state):
    rotate_cube_face(cube_state, 2, clockwise=True)
    # rotate the edges
    temp = cube_state[0][2].copy()  # save top row of U
    cube_state[0][2] = np.flipud(cube_state[4][:, 2])  # L right column -> U bottom row (flipped)
    cube_state[4][:, 2] = cube_state[3][0]  # D top row -> L right column
    cube_state[3][0] = np.flipud(cube_state[1][:, 0])  # R left column -> D top row (flipped)
    cube_state[1][:, 0] = temp  # U top row -> R left column


# Rotate F counterclockwise
def rotate_front_counterclockwise(cube_state):
    rotate_cube_face(cube_state, 2, clockwise=False)
    # rotate the edges
    temp = cube_state[0][2].copy()  # save top row of U
    cube_state[0][2] = cube_state[1][:, 0]  # R left column -> U bottom row
    cube_state[1][:, 0] = np.flipud(cube_state[3][0])  # D top row -> R left column (flipped)
    cube_state[3][0] = cube_state[4][:, 2]  # L right column -> D top row
    cube_state[4][:, 2] = np.flipud(temp)  # U top row -> L right column (flipped)


# Rotate R clockwise
def rotate_right_clockwise(cube_state):
    rotate_cube_face(cube_state, 1, clockwise=True)
    # rotate the edges
    temp = cube_state[0][:, 2].copy()  # save right column of U
    cube_state[0][:, 2] = cube_state[2][:, 2]  # F right column -> U right column
    cube_state[2][:, 2] = cube_state[3][:, 2]  # D right column -> F right column
    cube_state[3][:, 2] = np.flipud(cube_state[5][:, 0])  # B left column -> D right column (flipped)
    cube_state[5][:, 0] = np.flipud(temp)  # U right column -> B left column (flipped)


# Rotate R counterclockwise
def rotate_right_counterclockwise(cube_state):
    rotate_cube_face(cube_state, 1, clockwise=False)
    # rotate the edges
    temp = cube_state[0][:, 2].copy()  # save right column of U
    cube_state[0][:, 2] = np.flipud(cube_state[5][:, 0])  # B left column -> U right column (flipped)
    cube_state[5][:, 0] = np.flipud(cube_state[3][:, 2])  # D right column -> B left column (flipped)
    cube_state[3][:, 2] = cube_state[2][:, 2]  # F right column -> D right column
    cube_state[2][:, 2] = temp  # U right column -> F right column


# Rotate L clockwise
def rotate_left_clockwise(cube_state):
    rotate_cube_face(cube_state, 4, clockwise=True)
    # rotate the edges
    temp = cube_state[0][:, 0].copy()  # save left column of U
    cube_state[0][:, 0] = np.flipud(cube_state[5][:, 2])  # B right column -> U left column (flipped)
    cube_state[5][:, 2] = np.flipud(cube_state[3][:, 0])  # D left column -> B right column (flipped)
    cube_state[3][:, 0] = cube_state[2][:, 0]  # F left column -> D left column
    cube_state[2][:, 0] = temp  # U left column -> F left column


# Rotate L counterclockwise
def rotate_left_counterclockwise(cube_state):
    rotate_cube_face(cube_state, 4, clockwise=False)
    # rotate the edges
    temp = cube_state[0][:, 0].copy()  # save left column of U
    cube_state[0][:, 0] = cube_state[2][:, 0]  # F left column -> U left column
    cube_state[2][:, 0] = cube_state[3][:, 0]  # D left column -> F left column
    cube_state[3][:, 0] = np.flipud(cube_state[5][:, 2])  # B right column -> D left column (flipped)
    cube_state[5][:, 2] = np.flipud(temp)  # U left column -> B right column (flipped)


# Rotate U clockwise
def rotate_up_clockwise(cube_state):
    rotate_cube_face(cube_state, 0, clockwise=True)
    # rotate the edges
    temp = cube_state[2][0].copy()  # save top row of F
    cube_state[2][0] = cube_state[1][0]  # R top row -> F top row
    cube_state[1][0] = np.flipud(cube_state[5][0])  # B top row -> R top row (flipped)
    cube_state[5][0] = np.flipud(cube_state[4][0])  # L top row -> B top row (flipped)
    cube_state[4][0] = temp  # F top row -> L top row


# Rotate U counterclockwise
def rotate_up_counterclockwise(cube_state):
    rotate_cube_face(cube_state, 0, clockwise=False)
    # rotate the edges
    temp = cube_state[2][0].copy()  # save top row of F
    cube_state[2][0] = cube_state[4][0]  # L top row -> F top row
    cube_state[4][0] = np.flipud(cube_state[5][0])  # B top row -> L top row (flipped)
    cube_state[5][0] = np.flipud(cube_state[1][0])  # R top row -> B top row (flipped)
    cube_state[1][0] = temp  # F top row -> R top row


# Rotate D counterclockwise
def rotate_down_counterclockwise(cube_state):
    rotate_cube_face(cube_state, 3, clockwise=False)
    # rotate the edges
    temp = cube_state[2][2].copy()  # save bottom row of F
    cube_state[2][2] = cube_state[1][2]  # R bottom row -> F bottom row
    cube_state[1][2] = np.flipud(cube_state[5][2])  # B bottom row -> R bottom row (flipped)
    cube_state[5][2] = np.flipud(cube_state[4][2])  # L bottom row -> B bottom row (flipped)
    cube_state[4][2] = temp  # F bottom row -> L bottom row


# Rotate D clockwise
def rotate_down_clockwise(cube_state):
    rotate_cube_face(cube_state, 3, clockwise=True)
    # rotate the edges
    temp = cube_state[2][2].copy()  # save bottom row of F
    cube_state[2][2] = cube_state[4][2]  # L bottom row -> F bottom row
    cube_state[4][2] = np.flipud(cube_state[5][2])  # B bottom row -> L bottom row (flipped)
    cube_state[5][2] = np.flipud(cube_state[1][2])  # R bottom row -> B bottom row (flipped)
    cube_state[1][2] = temp  # F bottom row -> R bottom row


# Rotate B clockwise
def rotate_back_clockwise(cube_state):
    rotate_cube_face(cube_state, 5, clockwise=True)
    # rotate the edges
    temp = cube_state[0][0].copy()  # save top row of U
    cube_state[0][0] = cube_state[1][:, 2]  # R right column -> U top row
    cube_state[1][:, 2] = np.flipud(cube_state[3][2])  # D bottom row -> R right column (flipped)
    cube_state[3][2] = cube_state[4][:, 0]  # L left column -> D bottom row
    cube_state[4][:, 0] = np.flipud(temp)  # U top row -> L left column (flipped)


# Rotate B counterclockwise
def rotate_back_counterclockwise(cube_state):
    rotate_cube_face(cube_state, 5, clockwise=False)
    # rotate the edges
    temp = cube_state[0][0].copy()  # save top row of U
    cube_state[0][0] = np.flipud(cube_state[4][:, 0])  # L left column -> U top row (flipped)
    cube_state[4][:, 0] = cube_state[3][2]  # D bottom row -> L left column
    cube_state[3][2] = np.flipud(cube_state[1][:, 2])  # R right column -> D bottom row (flipped)
    cube_state[1][:, 2] = temp  # U top row -> R right column


# orient whole cube on R counterclockwise
def x_down(cube_state):
    temp = cube_state[0].copy()
    cube_state[0] = np.flipud(cube_state[5])  # B (flipped) -> U
    cube_state[5] = np.flipud(cube_state[3])  # D (flipped) -> B
    cube_state[3] = cube_state[2]  # F -> D
    cube_state[2] = temp  # U -> F
    rotate_cube_face(cube_state, 1, clockwise=False)
    rotate_cube_face(cube_state, 4, clockwise=True)


# orient whole cube on R clockwise
def x_up(cube_state):
    temp = cube_state[0].copy()
    cube_state[0] = cube_state[2]  # F -> U
    cube_state[2] = cube_state[3]  # D -> F
    cube_state[3] = np.flipud(cube_state[5])  # B (flipped) -> D
    cube_state[5] = np.flipud(temp)  # U (flipped) -> B
    rotate_cube_face(cube_state, 1, clockwise=True)
    rotate_cube_face(cube_state, 4, clockwise=False)


# orient whole cube on U counterclockwise
def y_down(cube_state):
    temp = cube_state[2].copy()
    cube_state[2] = np.flipud(cube_state[1])  # R (flipped) -> F
    cube_state[1] = np.flipud(cube_state[5])  # B (flipped) -> R
    cube_state[5] = np.flipud(cube_state[4])  # L (flipped) -> B
    cube_state[4] = np.flipud(temp)  # F (flipped) -> L
    rotate_cube_face(cube_state, 0, clockwise=False)
    rotate_cube_face(cube_state, 3, clockwise=True)


# orient whole cube on U clockwise
def y_up(cube_state):
    temp = cube_state[2].copy()
    cube_state[2] = np.flipud(cube_state[4])  # L (flipped) -> F
    cube_state[4] = np.flipud(cube_state[5])  # B (flipped) -> L
    cube_state[5] = np.flipud(cube_state[1])  # R (flipped) -> B
    cube_state[1] = np.flipud(temp)  # F (flipped) -> R
    rotate_cube_face(cube_state, 0, clockwise=True)
    rotate_cube_face(cube_state, 3, clockwise=False)


# orient whole cube on F counterclockwise
def z_down(cube_state):
    temp = cube_state[0].copy()
    cube_state[0] = np.flipud(cube_state[4])  # L (flipped) -> U
    cube_state[4] = np.flipud(cube_state[3])  # D (flipped) -> L
    cube_state[3] = np.flipud(cube_state[1])  # R (flipped) -> D
    cube_state[1] = np.flipud(temp)  # U (flipped) -> R
    rotate_cube_face(cube_state, 2, clockwise=False)
    rotate_cube_face(cube_state, 5, clockwise=True)


# orient whole cube on F clockwise
def z_up(cube_state):
    temp = cube_state[0].copy()
    cube_state[0] = np.flipud(cube_state[1])  # R (flipped) -> U
    cube_state[1] = np.flipud(cube_state[3])  # D (flipped) -> R
    cube_state[3] = np.flipud(cube_state[4])  # L (flipped) -> D
    cube_state[4] = np.flipud(temp)  # U (flipped) -> L
    rotate_cube_face(cube_state, 2, clockwise=True)
    rotate_cube_face(cube_state, 5, clockwise=False)


def update_cube_state(cube_state, move):
    match move:
        case "R":
            rotate_right_clockwise(cube_state)
        case "R'":
            rotate_right_counterclockwise(cube_state)
        case "L":
            rotate_left_clockwise(cube_state)
        case "L'":
            rotate_left_counterclockwise(cube_state)
        case "U":
            rotate_up_clockwise(cube_state)
        case "U'":
            rotate_up_counterclockwise(cube_state)
        case "D":
            rotate_down_clockwise(cube_state)
        case "D'":
            rotate_down_counterclockwise(cube_state)
        case "F":
            rotate_front_clockwise(cube_state)
        case "F'":
            rotate_front_counterclockwise(cube_state)
        case "B":
            rotate_back_clockwise(cube_state)
        case "B'":
            rotate_back_counterclockwise(cube_state)
        case "M":
            rotate_right_counterclockwise(cube_state)
            rotate_left_clockwise(cube_state)
            x_up(cube_state)
        case "M'":
            rotate_right_clockwise(cube_state)
            rotate_left_counterclockwise(cube_state)
            x_down(cube_state)
        case "E":
            rotate_up_counterclockwise(cube_state)
            rotate_down_clockwise(cube_state)
            y_up(cube_state)
        case "E'":
            rotate_up_clockwise(cube_state)
            rotate_down_counterclockwise(cube_state)
            y_down(cube_state)
        case "S":
            rotate_front_counterclockwise(cube_state)
            rotate_back_clockwise(cube_state)
            z_up(cube_state)
        case "S'":
            rotate_front_clockwise(cube_state)
            rotate_back_counterclockwise(cube_state)
            z_down(cube_state)
        case _:
            raise ValueError("Invalid move", move)
    print_cube_state(get_color_str(cube_state.copy()))
    return cube_state


# eg. solution: "R' D2 R' U2 R F2 D B2 U' R F' U R2 D L2 D' B2 R2 B2 U' B2"
# parse the output of the solver (solution string) and translates it into a list of cube moves
# Each move is either a string (e.g., "R", "R'") or a list of two moves
# for double turns (e.g., "D2" → ["D", "D"])
def parse_moves(solution):
    moves = []
    for m in solution.split():
        if "2" in m:
            moves.append([m[0], m[0]])
        else:
            moves.append(m)
    return moves


# functions for debugging
def get_color_str(cube_state):
    map = {"U": "W", "R": "B", "F": "R", "D": "Y", "L": "G", "B": "O"}
    for (i, j, k), value in np.ndenumerate(cube_state):
        cube_state[i][j][k] = map[value]
    return cube_state


def print_cube_state(cube_state):
    # Printing the U face
    for i in range(3):
        print(" " * 17 + "|" + f" {str(cube_state[0][i])} " + "|")
    print(" " * 17 + "-" * 17)
    # Print L,F,R,B
    for i in range(3):
        row = " |"
        for j in [4, 2, 1, 5]:
            row += f" {str(cube_state[j][i])} " + "|"
        print(row)
    print(" " * 17 + "-" * 17)
    # Printing the D face
    for i in range(3):
        print(" " * 17 + "|" + f" {str(cube_state[3][i])} " + "|")
