mport re
import pandas as pd
from typing import List, Dict, Any

class DataExtractor:
    """
    A class for extracting various data types from text using regular expressions.
    """
 def __init__(self):
     # Email addresses regex
     self.email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
                             
     # URLs regex
     self.url_pattern = r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)'
                                                     
     # Phone numbers regex (covers multiple formats)
     self.phone_pattern = r'(?:\(?\d{3}\)?[-.\s]?)?\d{3}[-.\s]?\d{4}'
                                                                             
     # Credit card numbers regex (16 digits with spaces or dashes)
     self.cc_pattern = r'\b(?:\d{4}[-\s]?){3}\d{4}\b'
                                                                                                     
     # Time regex (both 24-hour and 12-hour formats)
     self.time_pattern = r'\b(?:(?:0?[1-9]|1[0-2]):[0-5][0-9]\s?(?:AM|PM|am|pm)|(?:2[0-3]|[01]?[0-9]):[0-5][0-9])\b'

     # HTML tags regex
     self.html_pattern = r'<[^>]+>'
                
     # Hashtags regex
     self.hashtag_pattern = r'#[A-Za-z0-9_]+'
                                        
     # Currency amounts regex
     self.currency_pattern = r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'

  
def extract_emails(self, text: str) -> List[str]:
    """Extract all email addresses from the text."""
    return re.findall(self.email_pattern, text)
                    
def extract_urls(self, text: str) -> List[str]:
    """Extract all URLs from the text."""
    return re.findall(self.url_pattern, text)
                                        
def extract_phone_numbers(self, text: str) -> List[str]:
    """Extract all phone numbers from the text."""
    return re.findall(self.phone_pattern, text)

def extract_credit_cards(self, text: str) -> List[str]:
    """Extract all credit card numbers from the text."""
    return re.findall(self.cc_pattern, text)
                    
def extract_times(self, text: str) -> List[str]:
    """Extract all time formats from the text."""
    return re.findall(self.time_pattern, text)
                                        
def extract_html_tags(self, text: str) -> List[str]:
    """Extract all HTML tags from the text."""
    return re.findall(self.html_pattern, text)

def extract_hashtags(self, text: str) -> List[str]:
    """Extract all hashtags from the text."""
    return re.findall(self.hashtag_pattern, text)
                    
def extract_currency(self, text: str) -> List[str]:
    """Extract all currency amounts from the text."""
    return re.findall(self.currency_pattern, text)

def extract_all(self, text: str) -> Dict[str, List[str]]:
    """Extract all data types from the text."""
    return {
            'emails': self.extract_emails(text),
            'urls': self.extract_urls(text),
            'phone_numbers': self.extract_phone_numbers(text),
            'credit_cards': self.extract_credit_cards(text),
            'times': self.extract_times(text),
            'html_tags': self.extract_html_tags(text),
            'hashtags': self.extract_hashtags(text),
            'currency': self.extract_currency(text)
            }

def extract_to_dataframe(self, text: str) -> pd.DataFrame:
    """Extract all data and return as a DataFrame with counts."""
    data = self.extract_all(text)
    result = []

    for data_type, items in data.items():
    for item in items:
    result.append({
        'data_type': data_type,
        'value': item
         })

    return pd.DataFrame(result)

# Example usage
if __name__ == "__main__":
    # Sample text containing various data types to extract
    sample_text = """
    Contact us at support@example.com or john.doe@company.co.uk for more information.
    Visit our website at https://www.example.com or https://subdomain.example.org/page.
    Call us at (123) 456-7890 or 987-654-3210 or 555.123.4567.
    Payment received for order #12345: $1,234.56 at 14:30 and another payment of $99.99 at 2:30 PM.
    Credit card details: 1234 5678 9012 3456 or 9876-5432-1098-7654.
    <div class="container">
    <p>This is a paragraph with a <a href="link.html">link</a></p>
    <img src="image.jpg" alt="description">
    </div>
    Follow us on social media with #WebDevelopment and #ThisIsAHashtag.
    """

    # Create an instance of DataExtractor
        extractor = DataExtractor()
            
    # Extract all data types
        results = extractor.extract_all(sample_text)
                        
    # Print results
        print("Extraction Results:")
        print("=" * 50)
        for data_type, items in results.items():
        print(f"\n{data_type.upper()}:")
        for item in items:
        print(f"  - {item}")

    # Create a DataFrame
    df = extractor.extract_to_dataframe(sample_text)
        print("\nDataFrame Output:")
        print("=" * 50)
        print(df)
                                
    # Count of each data type
        print("\nCount by data type:")
        print("=" * 50)
        print(df['data_type'].value_counts())

