# Sistema de Reconhecimento de Placas por OCR (Flask + OpenCV + Tesseract)

---

## 🎥 **Vídeo de Demonstração**
> **Link do YouTube:** *https://www.youtube.com/watch?v=BKnajnBOFi8*

---

## 👩‍🏫 **Integrantes**
| Nome Completo | RM | Turma |
|--------------|------|--------|
| *Lavinia Soo Hyun Park* | *RM555679* | *2TDSB* |
| *Caroline de Oliveira* | *RM559123* | *2TDSB* |
| *Giulia Correa Camillo* | *RM554473* | *2TDSB* |

---

## 📌 Descrição Geral do Projeto

Este projeto consiste em um **microserviço de detecção e leitura de placas de veículos** utilizando:

- **Flask** para construção da API
- **OpenCV** para processamento da imagem
- **Pytesseract** (OCR) para reconhecer caracteres
- **Pré-processamento** para melhorar a acurácia da leitura

A API recebe uma imagem (`JPEG`, `PNG` ou outro formato comum), realiza o **processamento da placa**, extrai o texto contido nela e retorna o valor **padronizado** da placa em formato JSON.

O objetivo do projeto é **automatizar a etapa de triagem / registro** de motos ou veículos, reduzindo erros humanos e agilizando o fluxo de cadastro.

---

## 🧠 Como Funciona

1. O usuário envia uma imagem através de uma requisição `POST` para `/upload`.
2. A imagem é convertida para matriz NumPy e processada pelo OpenCV:
   - Conversão para escala de cinza
   - Filtro bilateral para redução de ruído
   - Detecção de bordas com Canny
3. O texto presente na área da placa é lido pelo **Tesseract OCR**.
4. O texto é tratado, filtrado e padronizado para formato de placa.
5. A API retorna um JSON como:

```json
{
  "plate": "ABC1234"
}
