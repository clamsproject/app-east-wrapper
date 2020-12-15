from clams.serve import ClamsApp
from clams.restify import Restifier

from east_utils import *

class EAST_td(ClamsApp):
    def appmetadata(self):
        metadata = {"name": "EAST Text Detection",
                    "description": "This tool applies EAST test detection to the video or image.",
                    "vendor": "Team CLAMS",
                    "requires": [DocumentTypes.ImageDocument, DocumentTypes.VideoDocument],
                    "produces": [AnnotationTypes.BoundingBox]}
        return metadata

    def setupmetadata(self):
        return

    def sniff(self, mmif):
        # this mock-up method always returns true
        return True

    def annotate(self, mmif: Mmif) -> str:
        video_filenames = mmif.get_documents_by_type(DocumentTypes.VideoDocument)
        if video_filenames:
            mmif = self.annotate_video(mmif)
        else:
            image_filenames = mmif.get_documents_by_type(DocumentTypes.ImageDocument)
            if image_filenames:
                mmif = self.annotate_image(mmif)
        return str(mmif)

    @staticmethod
    def annotate_video(mmif: Mmif) -> Mmif:
        mmif = run_EAST_video(mmif)
        return mmif

    @staticmethod
    def annotate_image(mmif: Mmif) -> Mmif:
        mmif = run_EAST_image(mmif)
        return mmif

if __name__ == "__main__":
    td_tool = EAST_td()
    td_service = Restifier(td_tool)
    td_service.run()