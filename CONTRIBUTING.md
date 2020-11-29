# How to Contribute

## Branch Organization
You can submit all changes to the `staging branch`, where we do whole our tests for new features

## Flags for your branch

To keep the `staging branch` in a releasable state, breaking changes and experimental features must be gated behind a feature flag.

#### New Feature
Use this flag to create a branch for new features
 - `feature/feature_name`

#### Bug fix
Use this flag to fix some bug
- `bugfix/bug_name`

#### Edit something
Use this flag to edit something
- `edit/edit_name`

## Your First Pull Request

Working on your first Pull Request? You can learn how from this free video series:
<p align="center">
<a href="https://egghead.io/series/how-to-contribute-to-an-open-source-project-on-github">
How to Contribute to an Open Source Project on GitHub
</a>
</p>

## Sending a Pull Request
The developers is monitoring for pull requests. We will review your pull request and either merge it, request changes to it, or close it with an explanation.

**Before submitting a pull request, please make sure the following is done:**

1.  Fork  [the repository](https://github.com/dyohan9/python-pix)  and create your branch from  `master`.

2.  Run  `poetry install`  in the repository root.

3.  Make sure your code lints (`poetry run flake8`). 

4.  Make sure your code lints (`poetry run black pyypix`). 

5.  If everything is ready, send your PR to `staging branch`.

## License

- **[GPL-3.0 License](https://github.com/dyohan9/python-pix/blob/master/LICENSE)**
