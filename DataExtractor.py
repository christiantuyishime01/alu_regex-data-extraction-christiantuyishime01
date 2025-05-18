import re

class DataExtractor:
    def __init__(self, text):
        self.text = text

    def extract_emails(self):
    """Extracts email addresses from text.
    Matches patterns like:
    - user@example.com
    - firstname.lastname@company.co.uk
    """
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(email_pattern, self.text)

    def extract_urls(self):
            """
            Extracts URLs from text.
            Matches patterns like:
            - https://www.example.com
            - https://subdomain.example.org/page
            """
            url_pattern = r'https?://(?:www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(?:/[^\s]*)?'
            return re.findall(url_pattern, self.text)

    def extract_phone_numbers(self):
                """
                Extracts phone numbers in various formats:
                - (123) 456-7890
                - 123-456-7890
                - 123.456.7890
                """
                phone_pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
                return re.findall(phone_pattern, self.text)

    def extract_hashtags(self):
                """
                Extracts hashtags from text:
                - #example
                - #ThisIsAHashtag
                """
                hashtag_pattern = r'#\w+'
                return re.findall(hashtag_pattern, self.text)

    def extract_all(self):
                """
                Extracts all supported patterns and returns a dictionary of results
                """
                return {
                        'emails': self.extract_emails(),
                        'urls': self.extract_urls(),
                        'phone_numbers': self.extract_phone_numbers(),
                        'hashtags': self.extract_hashtags()
                        }

    # Example usage
    if __name__ == "__main__":
                sample_text ="""Contact us at support@example.com or sales@company.co.uk.
                Visit our website at https://www.example.com or check our blog at https://blog.example.org.
                Call us at (123) 456-7890, 123-456-7890, or 123.456.7890.
                Follow us on social media #example #ALU #ThisIsAHashtag.
                """

                extractor = DataExtractor(sample_text)
                results = extractor.extract_all()

                print("Extracted Data:")
                for data_type, items in results.items():
                    print(f"\n{data_type.replace('_', ' ').title()}:")
                    for item in items:
                        print(f"  - {item}")
