# MkDocs Usage

## Building the Documentation

To build the documentation, use the following command:

```sh
task mkdocs:build
```

## Serving the Documentation Locally

To preview the documentation locally, run:

```sh
task mkdocs:serve
```

## README.md file

The `README.md` file from the project root is automatically copied to the `docs` directory as `index.md` when using either of the commands above. Therefore, you do not need to manually create or include this file, as it will be ignored in the `docs` folder.
