{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "collapsed_sections": [
        "kNuP0SDUZMBY"
      ]
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "# Santander Dev Week 2023 (ETL com Python)"
      ],
      "metadata": {
        "id": "BPJQsTCULaC-"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "sdw2023_api_url = 'https://sdw-2023-prd.up.railway.app'"
      ],
      "metadata": {
        "id": "FKqLC_CWoYqR"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "NYydpX_GLRCB"
      },
      "outputs": [],
      "source": [
        "import pandas as pd\n",
        "\n",
        "df = pd.read_csv('SDW2023.csv')\n",
        "user_ids = df['UserID'].tolist()\n",
        "print(user_ids)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import requests\n",
        "import json\n",
        "\n",
        "def get_user(id):\n",
        "  response = requests.get(f'{sdw2023_api_url}/users/{id}')\n",
        "  return response.json() if response.status_code == 200 else None\n",
        "\n",
        "users = [user for id in user_ids if (user := get_user(id)) is not None]\n",
        "print(json.dumps(users, indent=2))"
      ],
      "metadata": {
        "id": "F5XOuCZGSTGw"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#!pip install openai"
      ],
      "metadata": {
        "id": "O--PCAObTQkK"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "openai_api_key = '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'"
      ],
      "metadata": {
        "id": "sUB1doiDTX3y"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import openai\n",
        "\n",
        "openai.api_key = openai_api_key\n",
        "\n",
        "def generate_ai_news(user):\n",
        "  completion = openai.ChatCompletion.create(\n",
        "    model=\"gpt-4\",\n",
        "    messages=[\n",
        "      {\n",
        "          \"role\": \"system\",\n",
        "          \"content\": \"Você é um especialista em markting bancário.\"\n",
        "      },\n",
        "      {\n",
        "          \"role\": \"user\",\n",
        "          \"content\": f\"Crie uma mensagem para {user['name']} sobre a importância dos investimentos (máximo de 100 caracteres)\"\n",
        "      }\n",
        "    ]\n",
        "  )\n",
        "  return completion.choices[0].message.content.strip('\\\"')\n",
        "\n",
        "for user in users:\n",
        "  news = generate_ai_news(user)\n",
        "  print(news)\n",
        "  user['news'].append({\n",
        "      \"icon\": \"https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg\",\n",
        "      \"description\": news\n",
        "  })"
      ],
      "metadata": {
        "id": "n1w78kNxTrZY"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}