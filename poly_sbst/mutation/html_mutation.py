
from poly_sbst.mutation.abstract_mutation import AbstractMutation
from poly_sbst.generators.html_suite_generator import HTMLTestSuiteGenerator 
import random



class HTMLTestSuiteMutation(AbstractMutation):
    
    def __init__(self, mut_rate: float = 0.1, generator= HTMLTestSuiteGenerator):
        super().__init__(generator)
        self.mut_rate = mut_rate
        self.generator = generator
        self.mutators = [self.insert_random_tag, self.delete_random_tag,self.modify_random_attribute,
                         self.inject_malicious_script, self.add_whitespace]

    def _do_mutation(self, x):
        x=list(x)
        # mutate the test 
        try:
            for i in range(len(x)):
                mutator = random.choice(self.mutators)
                if random.random() <= self.mut_rate:
                    x[i] = mutator(x[i])
        except:
            pass
        return x
        
    def insert_random_tag(self, input_html):
        # Insert a random HTML tag at a random position
        tags = ['<div>', '<span>', '<a>', '<img>', '<script>', '<iframe>']
        random_tag = random.choice(tags)
        position = random.randint(0, len(input_html))
        mutated_input = input_html[:position] + random_tag + input_html[position:]
        return mutated_input

    def delete_random_tag(self, input_html):
        # Delete a random HTML tag
        tags_indices = [i for i, char in enumerate(input_html) if char == '<']
        if tags_indices:
            random_index = random.choice(tags_indices)
            end_tag_index = input_html.find('>', random_index)
            mutated_input = input_html[:random_index] + input_html[end_tag_index+1:]
        else:
            mutated_input = input_html
        return mutated_input

    def modify_random_attribute(self, input_html):
        # Modify a random attribute value in a random tag
        tag_start_indices = [i for i, char in enumerate(input_html) if char == '<']
        if tag_start_indices:
            random_index = random.choice(tag_start_indices)
            end_tag_index = input_html.find('>', random_index)
            tag = input_html[random_index:end_tag_index+1]
            tag_split = tag.split(' ')
            if len(tag_split) > 1:  # If the tag has attributes
                attribute_index = random.randint(1, len(tag_split)-1)
                attribute = tag_split[attribute_index]
                attribute_parts = attribute.split('=')
                if len(attribute_parts) == 2:  # If attribute has a value
                    attribute_parts[1] = '"modified_value"'
                    modified_attribute = '='.join(attribute_parts)
                    mutated_tag = tag.replace(attribute, modified_attribute)
                    mutated_input = input_html[:random_index] + mutated_tag + input_html[end_tag_index+1:]
                else:
                    mutated_input = input_html
            else:
                mutated_input = input_html
        else:
            mutated_input = input_html
        return mutated_input

    def inject_malicious_script(self, input_html):
        # Inject a malicious JavaScript script
        script = '<script>alert("XSS attack!");</script>'
        position = random.randint(0, len(input_html))
        mutated_input = input_html[:position] + script + input_html[position:]
        return mutated_input

    def add_whitespace(self, input_html):
        # Add random whitespace characters
        whitespace = ' ' * random.randint(1, 10)
        position = random.randint(0, len(input_html))
        mutated_input = input_html[:position] + whitespace + input_html[position:]
        return mutated_input