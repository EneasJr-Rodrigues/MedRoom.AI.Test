from med.room.utils import logger
import pandas as pd


JSON = {'indices_id': ['0','1','2','3'],
         'Frase original': ['Olhando para a escala na',
                           'Olhando para a escala na',
                           'Olhando para a escala na',
                           'Olhando para a escala na'],
         'Frases comparativas': ['De acordo com a escala de dor', 
                                'qual valor você acha que mais',
                                'De 0 a 10, qual o nível de',
                                'Qual a intensidade da sua dor?'],
         }

def generate_dataset(JSON):
    dataset = pd.DataFrame(JSON)
    logger.info(f'dataframe de teste: \n {dataset}')
    return dataset