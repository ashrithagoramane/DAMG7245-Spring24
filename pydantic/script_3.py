from bs4 import BeautifulSoup

tei_doc = './xml/sample.pdf.tei.xml'
with open(tei_doc, 'r') as tei:
    soup = BeautifulSoup(tei, 'xml')

def read_tei(tei_file):
    with open(tei_file, 'r') as tei:
        soup = BeautifulSoup(tei, 'xml')
        return soup
    raise RuntimeError('Cannot generate a soup from the input')

soup = read_tei(tei_doc)

def elem_to_text(elem, default=''):
    if elem:
        return elem.getText()
    else:
        return default
    
from dataclasses import dataclass

@dataclass
class Author:
    firstname: str
    middlename: str
    surname: str
    
turing_author = Author(firstname='Alan', middlename='M', surname='Turing', age=1)
print(f"{turing_author.firstname} {turing_author.surname} authored many influential publications in computer science.")


class TEIFile(object):
    def __init__(self, filename):
        self.filename = filename
        self.soup = read_tei(filename)
        self._text = None
        self._title = ''
        self._abstract = ''

    @property
    def doi(self):
        idno_elem = self.soup.find('idno', type='DOI')
        if not idno_elem:
            return ''
        else:
            return idno_elem.getText()

    @property
    def title(self):
        if not self._title:
            self._title = self.soup.title.getText()
        return self._title

    @property
    def abstract(self):
        if not self._abstract:
            abstract = self.soup.abstract.getText(separator=' ', strip=True)
            self._abstract = abstract
        return self._abstract

    @property
    def authors(self):
        authors_in_header = self.soup.analytic.find_all('author')
        result = []
        for author in authors_in_header:
            persname = author.persName
            if not persname:
                continue
            firstname = elem_to_text(persname.find("forename", type="first"))
            middlename = elem_to_text(persname.find("forename", type="middle"))
            surname = elem_to_text(persname.surname)
            person = Author(firstname=firstname, middlename=middlename, surname=surname)
            result.append(person)
        return result
    
    @property
    def text(self):
        if not self._text:
            divs_text = []
            for div in self.soup.body.find_all("div"):
                # div is neither an appendix nor references, just plain text.
                if not div.get("type"):
                    div_text = div.get_text(separator=' ', strip=True)
                    divs_text.append(div_text)

            plain_text = " ".join(divs_text)
            self._text = plain_text
        return self._text

tei = TEIFile(tei_doc)
print(f"The authors of the paper entitled '{tei.title}' are {tei.authors}")
