class Error:

    def __init__(self, error_text_brut: str):

        self.error_text_brut = error_text_brut
        self.program_name = ""
        self.output_message = ""

        self.error_location = error_text_brut[1:error_text_brut.index(")")].strip()

        self.error_line = self.error_location[:self.error_location.index(",")]

        self.error_type = error_text_brut[error_text_brut.index(")")+1:error_text_brut.index(":")].lower().strip()

        self.error_text = error_text_brut[error_text_brut.index(":")+1:].lower().strip()

    def set_program_name(self, program_name):
        self.program_name = program_name

    def error_analyser(self):
        """Détermine quel est le type de l'erreur et décide de quelle fonction lancer"""

        if (self.error_text.startswith("syntax error") and "expected" in self.error_text and
                self.error_text.endswith("found")):

            self.error_expected_found()

        elif self.error_text.startswith("error: identifier not found"):
            self.error_identifier_not_found()

        else:
            self.output_message += self.error_text_brut

    def error_missing_semicolon(self):
        self.output_message += (f"L\'erreur est a la ligne {self.error_line}. Tu as certainement oublié "
                                f"de mettre un point virgule a la ligne juste avant.\n")

    def error_semicolon_before_else(self):
        self.output_message += ("Quand vous utilisez un if else, il n'y a pas de point virgule derrière le end "
                                "qui précède le else\n"
                                f"Enlevez le point virgule derrière le \"end\" juste avant la ligne {self.error_line}")

    def error_identifier_not_found(self):
        identifier = self.error_text[self.error_text.index("\""):self.error_text.rindex("\"")]

        self.output_message += (f"Le mot clé {identifier} est inconnu. Si c'est une variable, vérifie qu'elle "
                                f"est initialisée")

    def error_missing_point_at_the_end(self):
        self.output_message += "Il faut mettre un point derrière le tout dernier \"end\" de votre programme"

    def error_illegal_expression(self):
        pass

    def error_expected_found(self):
        expected = self.error_text[self.error_text.index(",")+3:self.error_text.index("expected")-2].strip().lower()
        found = self.error_text[self.error_text.index("but")+5:self.error_text.index("found")-2].strip().lower()

        self.output_message += f"Le programme attendait \"{expected}\" mais a trouvé \"{found}\" a la place.\n\n"

        if expected == ".":
            self.error_missing_point_at_the_end()

        elif expected == ";":
            if found == "else":
                self.error_semicolon_before_else()

            else:
                self.error_missing_semicolon()

        elif expected == ":":
            if found == ")":
                self.error_missing_parameter_type()

            elif found == ";":
                self.error_missing_var_or_function_type()

    def error_missing_parameter_type(self):
        self.output_message += ("Vous avez probablement oublié de définir le type d'un paramètre d'une fonction. \n"
                                "Exemple: function NomFonction(Param1: Type; Param2: Type): TypeRenvoyéParLaFonction;")

    def error_missing_var_or_function_type(self):
        self.output_message += ("Vous avez probablement oublié de définir le type d'une variable ou d'une fonction. \n"
                                "Exemle pour une variable: \n"
                                "NomDeLaVariable: TypeDeLaVariable;\n\n"
                                "Exemple pour une fonction:\n"
                                "function NomFonction(Param1: Type; Param2: Type): TypeRenvoyéParLaFonction;")

    def __repr__(self):

        self.error_analyser()

        return (f"Il y a une erreur a la ligne {self.error_location}\n"
                f"{self.output_message}\n\n")


if __name__ == '__main__':
    erreur = Error("(273,9) Fatal: Syntax error, \";\" expected but \"identifier READLN\" found")
    # erreur.error_analyser()



################################
##   Crée par Téo Landsmann   ##
################################