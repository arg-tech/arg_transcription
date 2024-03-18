import json

class BertTEOutput:
    @staticmethod
    def format_output(transcript=None, dialog=True):
        locutions, nodes, edges, schemefulfillments, descriptorfulfillments, participants = [],[], [], [], [], []
        aif = {"nodes":nodes, "edges":edges, "locutions":locutions}
        ova ={"firstname": "", "surname": "", "url": "", "nodes": [], "edges": [] }
        x_aif = {
            "AIF":aif,
            "text":transcript,
            "dialog":dialog,
            "OVA":ova
            }
        return json.dumps(x_aif)

