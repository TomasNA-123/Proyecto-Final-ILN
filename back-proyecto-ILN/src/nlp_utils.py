import stanza
import langid
from transformers import pipeline
import torch
from .config import SENTIMENT_MODEL, RATING_MODEL

# Monkey patch torch.load for compatibility with PyTorch 2.6+
original_torch_load = torch.load
def patched_torch_load(*args, **kwargs):
    kwargs['weights_only'] = False
    return original_torch_load(*args, **kwargs)
torch.load = patched_torch_load

# NLP pipelines 
nlp_en = None
nlp_es = None
sentiment_pipeline_global = None
rating_pipeline_global = None

def initialize_pipelines():
    """Initialize all NLP pipelines only if they haven't been initialized yet"""
    global nlp_en, nlp_es, sentiment_pipeline_global, rating_pipeline_global
    
    # Initialize stanza pipelines
    if nlp_en is None or nlp_es is None:
        stanza.download('es')
        nlp_en = stanza.Pipeline(lang='en', processors='tokenize,ner,pos,mwt,lemma')
        nlp_es = stanza.Pipeline(lang='es', processors='tokenize,ner,pos,mwt,lemma')
    
    # Initialize transformers pipelines
    if sentiment_pipeline_global is None:
        sentiment_pipeline_global = pipeline(model=SENTIMENT_MODEL)
    
    if rating_pipeline_global is None:
        rating_pipeline_global = pipeline(model=RATING_MODEL)

def detect_language(text):
    """Detect the language of the input text."""
    lang, _ = langid.classify(text)
    return lang

def get_nlp_pipeline(lang):
    """Get the appropriate NLP pipeline based on language."""
    global nlp_en, nlp_es
    
    # Ensure pipelines are initialized
    if nlp_en is None or nlp_es is None:
        initialize_pipelines()
        
    return nlp_es if lang == 'es' else nlp_en

def extract_locations(doc):
    """Extract location entities from a Stanza document."""
    return [ent.text for ent in doc.ents if ent.type in ['LOC', 'GPE', 'FAC']]

def extract_nouns(doc):
    """Extract noun lemmas from a Stanza document."""
    nouns = []
    for sentence in doc.sentences:
        for word in sentence.words:
            if word.upos == 'NOUN':
                nouns.append(word.lemma)
    return nouns

def analyze_sentiment(text):
    """Analyze the sentiment of the input text."""
    global sentiment_pipeline_global
    
    result = sentiment_pipeline_global(text)
    return 'desc' if result[0]['label'] == 'positive' else 'asc'

def analyze_ratings(tips):
    """Analyze the ratings of tips using multilingual BERT."""
    global rating_pipeline_global
    
    processed_tips = [remove_special_characters(tip) for tip in tips]
    tip_ratings = rating_pipeline_global(processed_tips)
    
    ratings = []
    for tip_rating in tip_ratings:
        ratings.append(int(tip_rating['label'][0]))
    
    return sum(ratings) / len(ratings) if ratings else 0

def remove_special_characters(text):
    """Remove special characters from text while keeping punctuation."""
    keep_special_chars = ',.¡!¿?'
    chars_to_remove = ''.join(c for c in set(text) 
                             if not c.isalnum() and c != ' ' and c not in keep_special_chars)
    trans_table = str.maketrans('', '', chars_to_remove)
    return text.translate(trans_table) 