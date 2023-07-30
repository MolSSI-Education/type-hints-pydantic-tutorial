# Python Type Hints, Dataclasses, and Pydantic - MolSSI Hands-on Tutorial

Do more with structured and named data than putting everything into a Dictionary. 
Learn about Python type hints for arguments and variables to tell users what to expect. 
Structure data into Dataclasses for functional named data handlers. 
Leverage validation and the powerful third party tool pydantic to handle complex schema and automatic validation.

## Usage

### Building the book

If you'd like to develop on and build the Scientific Visualization using Python book, you should:

- Clone this repository and run
- Run `pip install -r requirements.txt` (it is recommended you do this within a virtual environment)
- (Recommended) Remove the existing `python-type-hints-and-pydantic/_build/` directory
- Run `jupyter-book build python-type-hints-and-pydantic/`

A fully-rendered HTML version of the book will be built in `python-type-hints-and-pydantic/_build/html/`.

### Hosting the book

The html version of the book is hosted on the `gh-pages` branch of this repo. A GitHub actions workflow has been created that automatically builds and pushes the book to this branch on a push or pull request to main.

If you wish to disable this automation, you may remove the GitHub actions workflow and build the book manually by:

- Navigating to your local build; and running,
- `ghp-import -n -p -f python-type-hints-and-pydantic/_build/html`

This will automatically push your build to the `gh-pages` branch. More information on this hosting process can be found [here](https://jupyterbook.org/publish/gh-pages.html#manually-host-your-book-with-github-pages).

## Contributors

We welcome and recognize all contributions. You can see a list of current contributors in the [contributors tab](https://github.com/janash/molssi_python_visualization/graphs/contributors).

## Credits

This project is created using the excellent open source [Jupyter Book project](https://jupyterbook.org/) and the [executablebooks/cookiecutter-jupyter-book template](https://github.com/executablebooks/cookiecutter-jupyter-book).
