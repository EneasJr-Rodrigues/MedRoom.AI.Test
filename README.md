# Natural Language Processing - Models Similariting Words

[![Documentation](https://img.shields.io/badge/docs-0.0.8-orange.svg?style=flat-square)](https://google.com)
[![Python required version: 3.8](https://img.shields.io/badge/python-3.8-blue.svg?style=flat-square)](https://www.python.org/downloads/release/python-370)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Model of a library for Natural Language Processing and Machine Learning applied to Computational Linguistics.

[Inner-Source](https://en.wikipedia.org/wiki/Inner_source) project. Please feel free to fix bugs, add new functionalities and tools. If you do so, please add your name to the list of contributors down below.

## ⚠️ Attention!

This project needed to install docker and docker-compose to run
If there is any update on this lib, the version must be updated on this file :)

Please follow that steps: [docker](https://docs.docker.com/engine/install/ubuntu/) and [docker-compose](https://docs.docker.com/compose/install/) to install.

Thanks 😄

## Usage

```shell
$docker-compose --env-file config/local/.env build
$docker-compose --env-file config/local/.env up -d **to up container** # A local jupyter server is now
             # available at localhost:8081
$docker-compose --env-file config/local/.env down **if you want off container**

```

## Install API from packages

If you want to use this project in another ambiente, you can to install using the down command. e.g: Use the API in google colab or another notebook

```shell
* In terminal
pip install MedRoom.AI.Test

```

### Exemples of call methodos after API installed:

```shell
from med.room.processors.class_principal import CallMethods
from med.room.processors.data_views import DataVisualizer
from med.room.processors.transform_data import NedRoomClean
from med.room.utils import logger

```

### Declare Variables to use in your analysis

```shell
filename = 'dados_frases'
column_text = ['Frase original', 'Frases comparativas']
additional_stop_words = ['bom', 'dia', 'ola', 'eu']
especifc_word_similar = 'dor'
title_of_plot_first = 'Similar words from text'
list_of_relationship_positive = ["acordo", "melhor"]
list_of_relationship_negative = ['dor', 'intensidade']

#target_sentence = "You'd love to drink a cool refreshing Coke"
target_sentence = ["Olhando para a escala na parede, qual valor indicaria melhor a sua dor hoje?",
                  "De acordo com a escala de dor ali na parede",
                  'qual valor você acha que mais representa a sua dor?',
                                'De 0 a 10, qual o nível de intensidade da sua dor atualmente?',
                                'Qual a intensidade da sua dor?']
```

### Call Class Principal

```shell
dataset, model_similar, matrix_words, dataframe_matrix, model, embeddings_en_2d, print_info, similar, word_clusters, w2v_vocab_result, result = CallMethods.call_processors(filename=filename,
                                                column_text=column_text,
                                                additional_stop_words=additional_stop_words,
                                                especifc_word_similar=especifc_word_similar,
                                                list_of_relationship_positive=list_of_relationship_positive,
                                                list_of_relationship_negative=list_of_relationship_negative,
                                                target_sentence=target_sentence)

```

### plot graph views

```shell
DataVisualizer.tsne_plot_similar_words(title_of_plot_first, matrix_words, embeddings_en_2d, word_clusters, 0.7, 'similar_words.png')

```

### Maps of Words Relationship

```shell
DataVisualizer.plo_similar_between_words(dataframe_matrix)
```

### Dimension Mapa

```shell
DataVisualizer.dimensional_vector_words(model, matrix_words, especifc_word_similar)
```

### Black Formatter

[Comand Line Black Option](https://github.com/psf/black#command-line-options)

> Ignore the formatter black in code row or function

```python

# fmt: off
def func(x, b):
    return x * b

```

## Current functionalities:

Natural Language Extractor:

* Cleaner

Natural Language Transformer:

* Word2Vec

Natural Language Model:

* t-SNE

## Main Contributors (until mar/2023- please join us!)

* Eneas Rodrigues de Souza Junior - eneas.rodrigues25@gmail.com
