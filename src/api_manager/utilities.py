from pydantic import BaseModel
from typing import List
"""
- if the probability is higher than 60%:
   [GIVEN_NAME] is mostly certain to be from [COUNTRY_NAME]

- if the probability is between 30% and 60%:
   [GIVEN_NAME] may be from [COUNTRY_NAME]

- if the probability is below 30%:
   It seems that [GIVEN_NAME] is from [COUNTRY_NAME]. But I'm just guessing!"""


class DesiredOutput(BaseModel):
    name: str
    probability: float
    country_name: str

    def to_string(self):
        if self.probability > .6:
            return f"{self.name} is mostly certain to be from {self.country_name}<br>"
        elif .3 <= self.probability <= .6:
            return f"{self.name} may be from {self.country_name}<br>"
        else:
            return f"It seems that {self.name} is from {self.country_name}. But I'm just guessing!<br>"


def prettify_content(desired_output_dict: List[DesiredOutput]) -> str:
    pretty_out = ""
    for d in desired_output_dict:
        pretty_out += d.to_string()
    return pretty_out if pretty_out != "" else f"Sorry no match found for {desired_output_dict[0].name}"
