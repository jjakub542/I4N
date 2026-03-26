from django.core.management.base import BaseCommand
from verification.models import Statement, Tag
from django.utils import timezone

MOCK_STATEMENTS = [
    {
        "title": "Koszty budowy elektrowni jądrowej w Polsce",
        "quote": "„Energia jądrowa jest droższa od węgla nawet przy uwzględnieniu kosztów emisji CO₂.”",
        "text": "Wypowiedź dotyczy porównania kosztów budowy elektrowni jądrowych i węglowych...",
        "author_name": "Marcin Kowalski",
        "author_role": "Lewica",
        "read_time_minutes": 5,
        "status": "false",
        "tags": ["koszty", "emisje", "polityka"],
    },
    {
        "title": "Pierwszy reaktor w Polsce ruszy w 2033 roku",
        "quote": "„Polska uruchomi swój pierwszy reaktor jądrowy w 2033 roku.”",
        "text": "Rząd deklaruje, że pierwszy blok jądrowy zostanie uruchomiony w 2033 roku...",
        "author_name": "Anna Nowak",
        "author_role": "Ministerstwo Klimatu",
        "read_time_minutes": 4,
        "status": "unverified",
        "tags": ["polityka", "reaktory"],
    },
    {
        "title": "SMR-y skracają czas budowy o 70%",
        "quote": "„Małe reaktory modułowe można zbudować o 70% szybciej niż duże elektrownie.”",
        "text": "Firmy promujące SMR-y podkreślają krótszy czas budowy dzięki prefabrykacji...",
        "author_name": "Tomasz Zieliński",
        "author_role": "Ekspert energetyczny",
        "read_time_minutes": 6,
        "status": "in_progress",
        "tags": ["technologia", "smr"],
    },
    {
        "title": "Promieniowanie przy elektrowniach jest niższe niż tło naturalne",
        "quote": "„Mieszkańcy okolic elektrowni jądrowych otrzymują mniejszą dawkę promieniowania niż z natury.”",
        "text": "Badania wykazują, że emisje promieniowania z elektrowni jądrowych są minimalne...",
        "author_name": "Instytut Bezpieczeństwa Jądrowego",
        "author_role": "Organizacja naukowa",
        "read_time_minutes": 3,
        "status": "true",
        "tags": ["promieniowanie", "bezpieczeństwo"],
    },
    {
        "title": "Odpady jądrowe są niebezpieczne przez 100 000 lat",
        "quote": "„Zużyte paliwo jądrowe pozostaje śmiertelnie niebezpieczne przez 100 tysięcy lat.”",
        "text": "Wypowiedź dotyczy czasu rozpadu izotopów w odpadach jądrowych...",
        "author_name": "EkoZiemia",
        "author_role": "Organizacja ekologiczna",
        "read_time_minutes": 5,
        "status": "misleading",
        "tags": ["odpady", "bezpieczeństwo"],
    },
    {
        "title": "Energia jądrowa jest najtańsza w Europie",
        "quote": "„Atom to obecnie najtańsze źródło energii w całej Unii Europejskiej.”",
        "text": "Wypowiedź dotyczy porównania kosztów LCOE różnych technologii...",
        "author_name": "Europejski Instytut Energii",
        "author_role": "Think tank",
        "read_time_minutes": 4,
        "status": "false",
        "tags": ["ekonomia", "polityka"],
    },
    {
        "title": "Reaktory fuzyjne będą komercyjne do 2040 roku",
        "quote": "„Do 2040 roku energia z fuzji będzie dostępna komercyjnie.”",
        "text": "Startupy technologiczne deklarują szybki postęp w technologii fuzji...",
        "author_name": "FusionX Labs",
        "author_role": "Startup technologiczny",
        "read_time_minutes": 6,
        "status": "unverifiable",
        "tags": ["fuzja", "technologia"],
    },
    {
        "title": "Elektrownie jądrowe emitują zero CO₂",
        "quote": "„Elektrownie jądrowe nie emitują CO₂ podczas pracy.”",
        "text": "Wypowiedź dotyczy emisji operacyjnych elektrowni jądrowych...",
        "author_name": "Międzynarodowa Agencja Energii",
        "author_role": "Agencja międzynarodowa",
        "read_time_minutes": 3,
        "status": "true",
        "tags": ["emisje", "klimat"],
    },
    {
        "title": "Jeden SMR zasili milion domów",
        "quote": "„Jeden mały reaktor modułowy może zasilić milion gospodarstw domowych.”",
        "text": "Deklaracje producentów SMR-ów często dotyczą maksymalnych parametrów...",
        "author_name": "NextGen Reactors",
        "author_role": "Producent technologii",
        "read_time_minutes": 4,
        "status": "in_progress",
        "tags": ["smr", "technologia"],
    },
    {
        "title": "Czarnobyl nadal wpływa na żywność w Europie",
        "quote": "„W wielu krajach Europy żywność nadal jest skażona po katastrofie w Czarnobylu.”",
        "text": "Wypowiedź dotyczy poziomów cezu-137 w produktach rolnych...",
        "author_name": "Daily Europe News",
        "author_role": "Media",
        "read_time_minutes": 5,
        "status": "misleading",
        "tags": ["promieniowanie", "wypadki"],
    },
]

class Command(BaseCommand):
    help = "Load mock nuclear-energy verification data"

    def handle(self, *args, **options):
        self.stdout.write("Loading mock statements...")

        for item in MOCK_STATEMENTS:
            # Create or get tags
            tag_objects = []
            for tag_name in item["tags"]:
                tag_obj, _ = Tag.objects.get_or_create(name=tag_name)
                tag_objects.append(tag_obj)

            # Create statement
            statement = Statement.objects.create(
                title=item["title"],
                quote=item["quote"],
                text=item["text"],
                author_name=item["author_name"],
                author_role=item["author_role"],
                read_time_minutes=item["read_time_minutes"],
                status=item["status"],
                created_at=timezone.now(),
            )

            # Add tags
            statement.tags.set(tag_objects)

        self.stdout.write(self.style.SUCCESS("Mock data loaded successfully!"))
