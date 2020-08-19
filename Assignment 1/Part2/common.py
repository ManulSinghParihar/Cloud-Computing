{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "CloudA2P2.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ManulSinghParihar/Cloud-Computing/blob/master/CloudA2P2.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "2TFeF6F4Hk3b",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 123
        },
        "outputId": "5e295e8e-30e0-4fb2-e843-25e4c3d7375f"
      },
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ],
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Mounted at /content/drive\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "iHaNGlfTJ92d",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "e5aae60c-d6f4-4ea1-b57b-23d043ce0b87"
      },
      "source": [
        "cd '/content/drive/My Drive/Colab Notebooks'"
      ],
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "/content/drive/My Drive/Colab Notebooks\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "RFTzf86ZLdo_",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "def wordCount(contents):\n",
        "  d = {}\n",
        "  for line in contents.split(', \\'.|_|-|!'):\n",
        "    line = line.lower() \n",
        "    words = line.split(\" \")\n",
        "    for word in words:\n",
        "      if word.isnumeric():\n",
        "        continue\n",
        "      if word[-1] == '.' or word[-1] == ',' or word[-1] == '\\'' or word[-1] == ')':\n",
        "        word = word[:-1]\n",
        "      if word[0] == '\\'' or word[0] == '(':\n",
        "        word = word[1:]\n",
        "      if word in d: \n",
        "        d[word] = d[word] + 1\n",
        "      else: \n",
        "        d[word] = 1\n",
        "  return d"
      ],
      "execution_count": 4,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "bqMq0KK5Lenb",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "def topTenWords(d):\n",
        "  s = sorted(d.items(), key=lambda x: x[1], reverse=True)\n",
        "  count = 0\n",
        "  for i in s:\n",
        "    if count<10:\n",
        "      print(i[0],\"\\t\\t:\\t\", i[1])\n",
        "      count += 1\n",
        "    else:\n",
        "      break"
      ],
      "execution_count": 5,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "iT-K0--WHwN0",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "def readFile(path):\n",
        "    with open(path, 'r') as f:\n",
        "        return f.read()"
      ],
      "execution_count": 6,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "nW8ylOduHzC5",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 189
        },
        "outputId": "c5ac1a9c-1a08-42cc-8a59-d37dc82c0098"
      },
      "source": [
        "path = \"sample.txt\"\n",
        "contents = readFile(path)\n",
        "d = wordCount(contents)\n",
        "topTenWords(d)"
      ],
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "the \t\t:\t 11\n",
            "of \t\t:\t 9\n",
            "a \t\t:\t 8\n",
            "lorem \t\t:\t 8\n",
            "ipsum \t\t:\t 8\n",
            "to \t\t:\t 5\n",
            "it \t\t:\t 4\n",
            "is \t\t:\t 3\n",
            "by \t\t:\t 3\n",
            "content \t\t:\t 3\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}
