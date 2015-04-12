// Created 4/9/2015
// Demonstrates DFS/Backtracing in Java
// Run with Java 1.6+

public class DFS {

    static final int WIDTH = 5;
    static final int HEIGHT = 5;

    static int[][] grid = new int[WIDTH][HEIGHT];
    public static void main(String[] args) {
        // setup initial grid, 1 indicates walkable
        grid[0][1] = 1;
        grid[0][2] = 1;
        grid[1][0] = 1;
        grid[2][0] = 1;
        grid[1][1] = 1;
        grid[0][3] = 1;
        grid[1][4] = 1;
        grid[1][2] = 1;

        depthFirstSearch(0, 1);
    }

    // perform DFS starting at location [r][c]
    public static void depthFirstSearch(int r, int c) {
        // out of bonuds
        if(r >= HEIGHT || r < 0 || c >= WIDTH || c < 0) {
            return;
        }
        System.out.println("row: " + r + ", col: " + c);
    
        // already visited or can't walk there
        if(grid[r][c] == 0 || grid[r][c] == 2) {
            if(grid[r][c] == 0)
                System.out.println("Can't walk here.\n");
            else
                System.out.println("Already visited here\n");
            return;
        }
        grid[r][c] = 2;

        printGrid();

        // recursive calls to next 4 states
        depthFirstSearch(r + 1, c); // down
        depthFirstSearch(r - 1, c); // up
        depthFirstSearch(r, c + 1); // right
        depthFirstSearch(r, c - 1); // left
    }

    // print out global grid variable
    public static void printGrid() {
        for(int i = 0; i < HEIGHT; i++) {
            for(int j = 0; j < WIDTH; j++) {
                System.out.print(grid[i][j] + " ");
            }
            System.out.println();
        }

        System.out.println();
    }
}
