import pandas as pd
import matplotlib.pyplot as plt
import argparse


def main(input_file, output_file):

    df = pd.read_csv(input_file)
    # print(df.head())

    boundingBox = (df.x.min(),   df.x.max(),
                   df.y.min(), df.y.max())

    # print(boundingBox)

    kaartVanNederland = plt.imread(
        'Afbeeldingen/nederlandKaartZonderSteden.png')

    fig, ax = plt.subplots(figsize=(8, 7))

    ax.scatter(df.x, df.y, zorder=1, alpha=0.2, c='b', s=10)
    ax.set_title('Plotting coordinates')
    ax.set_xlim(boundingBox[0], boundingBox[1])
    ax.set_ylim(boundingBox[2], boundingBox[3])
    ax.imshow(kaartVanNederland, zorder=0, extent=boundingBox, aspect='equal')

    plt.savefig(output_file, format='png')


if __name__ == "__main__":
    # Set-up parsing command line arguments
    parser = argparse.ArgumentParser(description="plots a graph from the data")

    # Adding arguments
    parser.add_argument("input", help="location of datafile")
    parser.add_argument("output", help="location of output file")

    # Read arguments from command line
    args = parser.parse_args()

    # Run main with provide arguments
    main(args.input, args.output)
