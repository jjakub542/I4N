from django.core.management.base import BaseCommand
from verification.models import Statement, Tag
from django.utils import timezone

MOCK_STATEMENTS = [
    {
        "title": "Poland will operate its first nuclear reactor by 2033",
        "text": "The government claims that the first large-scale nuclear reactor will be operational by 2033 as part of the national energy strategy.",
        "author": "Ministry of Climate and Environment",
        "status": "unverified",
        "tags": ["policy", "reactors", "energy strategy"],
    },
    {
        "title": "SMR reactors reduce construction time by 70%",
        "text": "Several companies promoting SMR technology state that modular construction shortens build time by up to 70% compared to traditional reactors.",
        "author": "EnergyTech Europe",
        "status": "in_progress",
        "tags": ["technology", "smr", "economics"],
    },
    {
        "title": "Radiation from nuclear plants is lower than natural background levels",
        "text": "A common claim is that radiation exposure near nuclear power plants is significantly lower than natural background radiation.",
        "author": "Nuclear Safety Institute",
        "status": "true",
        "tags": ["radiation", "safety"],
    },
    {
        "title": "Nuclear waste remains dangerous for 100,000 years",
        "text": "Environmental groups often state that spent nuclear fuel remains hazardous for up to 100,000 years and cannot be safely stored.",
        "author": "GreenFuture Coalition",
        "status": "misleading",
        "tags": ["waste", "safety", "environment"],
    },
    {
        "title": "Nuclear energy is the cheapest source of electricity in Europe",
        "text": "Some political figures argue that nuclear energy is currently the cheapest electricity source across the European Union.",
        "author": "European Energy Forum",
        "status": "false",
        "tags": ["economics", "policy"],
    },
    {
        "title": "Fusion reactors will be commercially viable by 2040",
        "text": "Tech startups claim that fusion power plants will enter commercial operation by 2040 thanks to rapid advances in plasma confinement.",
        "author": "FusionX Labs",
        "status": "unverifiable",
        "tags": ["fusion", "technology"],
    },
    {
        "title": "Nuclear plants emit zero CO₂ during operation",
        "text": "It is frequently stated that nuclear power plants produce no carbon dioxide during electricity generation.",
        "author": "International Energy Agency",
        "status": "true",
        "tags": ["climate", "emissions"],
    },
    {
        "title": "A single SMR can power 1 million homes",
        "text": "Some SMR vendors claim that one small modular reactor can supply electricity to one million households.",
        "author": "NextGen Reactors",
        "status": "in_progress",
        "tags": ["smr", "capacity", "technology"],
    },
    {
        "title": "Nuclear energy receives more subsidies than renewables",
        "text": "Critics argue that nuclear energy benefits from higher government subsidies than renewable energy sources.",
        "author": "Energy Policy Watch",
        "status": "unverified",
        "tags": ["economics", "policy"],
    },
    {
        "title": "Radiation from Chernobyl still affects food in Europe",
        "text": "Some media outlets claim that agricultural products across Europe still show harmful levels of radiation from the Chernobyl accident.",
        "author": "Daily Europe News",
        "status": "misleading",
        "tags": ["radiation", "accidents"],
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
                text=item["text"],
                author=item["author"],
                status=item["status"],
                created_at=timezone.now(),
            )

            # Add tags
            statement.tags.set(tag_objects)

        self.stdout.write(self.style.SUCCESS("Mock data loaded successfully!"))
