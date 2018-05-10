import tkinter
from tkinter import filedialog

def main():
    
    tkinter.Tk().withdraw() # Close the root window
    in_path = filedialog.askopenfilename()
    
    cumulative = 0
    highest_score = 0
    lowest_score = 1000
    var = {}
    line_counter = 0

    # Open file
    with open(in_path) as f:

        # Search through each line
        for line in f:

            # Only split the lines that contains 'score'
            if 'score' in line:
                var[line_counter] = line.split()

                # Grab the score at index 11
                cur_score = (int)( var[line_counter][11].strip("[]") )

                # Add to cumulative score
                cumulative += cur_score

                # Check if highest score
                if (cur_score > highest_score):
                   highest_score = cur_score

                # Check if lowest score
                if (cur_score < lowest_score):
                    lowest_score = cur_score

                # Increment line_counter
                line_counter = line_counter + 1

    # Add 1 to line_counter because line_counter started at 0 to make iterating easier            
    average = cumulative / ( line_counter + 1 )

    # Print stats
    print("Average score: {0:.2f}".format(average))
    print("Highest score: {0:.2f}".format(highest_score))
    print("Lowest score: {0:.2f}".format(lowest_score))
    print("Episodes: {}".format(line_counter + 1))

if __name__ == "__main__":
    main()