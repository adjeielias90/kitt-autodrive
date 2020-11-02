# Product Name
> Short blurb about what your product does.

[![Python Version][python-image]][npm-url]
[![Build Status][travis-image]][travis-url]
<!-- [![Downloads Stats][npm-downloads]][npm-url] -->

Behavioral Cloning and Reinforcement Learning for Autonomous Driving

<!-- ![](header.png) -->

## Installation

OS X & Linux:

```sh
pip install -r requirements.txt
```

## Runnning the source

Important: Please be sure to install all dependencies before you begin.

1. [Download the correct simulation for your OS](https://github.com/udacity/self-driving-car-sim)

2. Run the simulator in training mode with accepted parameters based on your system.

3. After driving accross the track, reverse course and drive back to your previous position.
Do this as many times as you can to get it right. After running the simulation you will notice a new
folder has been created with the traning_data. This folder contains the assets we will use to train our CNN.
The training data contains images of the track with their corresponding steering angles.

4. Now, after running the simulator, install all dependencies and run the driverCNN file
under the folder /behavioral_cloning to train your data.
Don't forget to include the training data before you begin.

5. After training, re-run your simulator this time in test_mode and start the the driver.py
located under the /behavioral_cloning folder.

Windows:

```sh
edit autoexec.bat
```

## Usage example

A few motivating and useful examples of how your product can be used. Spice this up with code blocks and potentially more screenshots.

_For more examples and usage, please refer to the [Wiki][wiki]._

## Development setup

Describe how to install all development dependencies and how to run an automated test-suite of some kind. Potentially do this for multiple platforms.

```sh
make install
npm test
```

## Release History

<!-- * 0.2.1
    * CHANGE: Update docs (module code remains unchanged)
* 0.2.0
    * CHANGE: Remove `setDefaultXYZ()`
    * ADD: Add `init()`
* 0.1.1
    * FIX: Crash when calling `baz()` (Thanks @GenerousContributorName!)
* 0.1.0
    * The first proper release
    * CHANGE: Rename `foo()` to `bar()` -->
* 0.0.1
    * Work in progress

## Meta

Your Name – [@eli_as_](https://twitter.com/@eli_as_)

Distributed under the MIT. See ``LICENSE`` for more information.

[https://github.com/adjeielias90/kitt-autodrive](https://github.com/adjeielias90/)

## Contributing

1. Fork it (<https://github.com/adjeielias90/kitt-autodrive/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->
<!-- [npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square -->
<!-- [npm-url]: https://npmjs.org/package/datadog-metrics -->
<!-- [npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square -->
<!-- [travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square -->
<!-- [travis-url]: https://travis-ci.org/dbader/node-datadog-metrics -->
<!-- [wiki]: https://github.com/yourname/yourproject/wiki -->