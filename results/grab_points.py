import tkinter
from tkinter import filedialog


def main():
    
    tkinter.Tk().withdraw() # Close the root window
    in_path = filedialog.askopenfilename() 

    var = {}
    plot = {}
    line_counter = 0

    # Open file
    with open(in_path) as f:

        # Search through each line
        for line in f:

            # Only split the lines that contains 'score'
            if 'score' in line:
                var[line_counter] = line.split()

                # Increment line_counter
                line_counter = line_counter + 1

    y = open("smart_y.txt", "w+")
    x = open("smart_x.txt", "w+")
    # Episode count 1
    i = 1
    cumulative = 0
                
    # Go through each score
    for index in list(var.values()):

        # Grab the score at index 11
        cur_score = (int)( index[11].strip("[]") )

        cumulative += cur_score

        # Increment episode
        i += 1
        
        # Get average every 1000 episodes
        if( i % 1000 == 0 ):
            average = cumulative / 1000
            cumulative = 0
            # Write to files
            y.write("{0:.2f}\n".format( average ) )
            x.write("{}\n".format( i ) )

    # Close files
    y.close()
    x.close()    
    
if __name__ == "__main__":
    main()