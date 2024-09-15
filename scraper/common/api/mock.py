from .interface import API, ApiResponse


class MockAPI(API):
    """Mock API for testing the pipeline with dummy data"""

    def scrape(self, _: str) -> ApiResponse:
        return {
            "events": [
                {
                    "end_date": "",
                    "end_time": "",
                    "event_attendence": "in-person",
                    "event_city": "",
                    "event_description": "Université Laval's Centre de recherche en données massives (CRDM) launches the first edition of its Colloque sur la cybersécurité.This event will bring together internationally renowned specialists, researchers, postdoctoral fellows and students, offering a unique plat ... ",
                    "event_name": "CRDM conference on cybersecurity",
                    "event_url": "/en/events/crdm-conference-cybersecurity",
                    "start_date": "2024-09-16",
                    "start_time": "",
                },
                {
                    "end_date": "",
                    "end_time": "",
                    "event_attendence": "online",
                    "event_city": "online",
                    "event_description": "Canada's immigration management is in the process of being profoundly transformed. Big data infrastructures, Artificial Intelligence (AI), and automated decision-making tools promise to eliminate backlogs, reduce long wait times, avoid administrative errors, and provide fa ... ",
                    "event_name": "The effects of automation and AI on immigration to Canada",
                    "event_url": "/en/events/effects-automation-and-ai-immigration-canada",
                    "start_date": "2024-09-27",
                    "start_time": "",
                },
                {
                    "end_date": "",
                    "end_time": "",
                    "event_attendence": "hybrid",
                    "event_city": "",
                    "event_description": "Third Conference in the Reading Club Series of the Law, Cyberjustice, and Cybersecurity Axis ",
                    "event_name": "Reading club",
                    "event_url": "/en/events/reading-club-0",
                    "start_date": "2024-10-04",
                    "start_time": "",
                },
                {
                    "end_date": "",
                    "end_time": "",
                    "event_attendence": "hybrid",
                    "event_city": "",
                    "event_description": "ADOR-IA is a unique opportunity to work with a multidisciplinary team to reflect on addressing the challenges of responsible AI development and operationalization.",
                    "event_name": "ADOR-IA",
                    "event_url": "/en/events/ador-ia",
                    "start_date": "2024-08-22",
                    "start_time": "",
                },
                {
                    "end_date": "",
                    "end_time": "",
                    "event_attendence": "online",
                    "event_city": "online",
                    "event_description": "Sous forme de panel, le lancement mettra en lumière certains auteurs et chapitres de l'ouvrage Intelligence artificielle, culture et média sous la direction de Véronique Guèvremont et Colette Brin.DescriptionLes nouveaux outils conversationnels ou générateurs d’œuv ... ",
                    "event_name": "Launch of Artificial Intelligence, Culture and Media",
                    "event_url": "/en/events/launch-artificial-intelligence-culture-and-media",
                    "start_date": "2024-06-14",
                    "start_time": "",
                },
                {
                    "end_date": "",
                    "end_time": "",
                    "event_attendence": "hybrid",
                    "event_city": "",
                    "event_description": "Obvia is pleased to invite you to the launch of the first edition of the État de la situation sur les impacts sociétaux de l'intelligence artificielle et du numérique.In a context of perpetual change, where technological advances are redefining our interactions and ins ... ",
                    "event_name": "Launch of the State of Play report on the societal impacts of artificial intelligence and digital technology",
                    "event_url": "/en/events/launch-state-play-report-societal-impacts-artificial-intelligence-and-digital-technology",
                    "start_date": "2024-06-13",
                    "start_time": "",
                },
                {
                    "end_date": "",
                    "end_time": "",
                    "event_attendence": "in-person",
                    "event_city": "",
                    "event_description": "Obvia's Scientific Department in charge of collaboration with industry aims to establish close collaboration between the various players in the industrial AI ecosystem, including developers, start-ups, SMEs, large corporations and academic organizations. Its main mission i ... ",
                    "event_name": "Action IA: Together for responsible development and adoption in industry",
                    "event_url": "/en/events/action-ia-together-responsible-development-and-adoption-industry",
                    "start_date": "2024-06-04",
                    "start_time": "",
                },
                {
                    "end_date": "",
                    "end_time": "",
                    "event_attendence": "hybrid",
                    "event_city": "",
                    "event_description": "As part of the Interdisciplinary Dialogues series, Obvia, IVADO and Mila invite you to the Rethinking Culture in the Age of AI panel on the challenges and impacts of generative AI on the cultural and creative industries. Moderated by Le Devoir editor Brian Myles, the panel ... ",
                    "event_name": "Interdisciplinary Dialogues: Rethinking culture in the age of AI",
                    "event_url": "/en/events/interdisciplinary-dialogues-rethinking-culture-age-ai",
                    "start_date": "2024-05-31",
                    "start_time": "",
                },
                {
                    "end_date": "",
                    "end_time": "",
                    "event_attendence": "hybrid",
                    "event_city": "",
                    "event_description": "This is the second in a series of lectures on key works in the field of law, cyberjustice and cybersecurity. In the form of a reading circle, Prof. Benoît Dupont will present his work, and a referee from another discipline, in this case Prof. Hugo Loiseau, will comment on ... ",
                    "event_name": "Reading club",
                    "event_url": "/en/events/reading-club",
                    "start_date": "2024-05-23",
                    "start_time": "",
                },
                {
                    "end_date": "",
                    "end_time": "",
                    "event_attendence": "in-person",
                    "event_city": "",
                    "event_description": "Are you passionate about the use of AI in politics? The Politics in the Age of Artificial Intelligence round table is for you! Organized as part of the Prix du livre politique, this discussion promises to spark lively debate between guest panelists Karine Gentelet, Jocelyn ... ",
                    "event_name": "Round table Politics in the age of artificial intelligence",
                    "event_url": "/en/events/round-table-politics-age-artificial-intelligence",
                    "start_date": "2024-05-22",
                    "start_time": "",
                },
            ],
        }
