import pyirk as p

__URI__ = "irk:/oee/0.1"
keymanager = p.KeyManager()
p.register_mod(__URI__, keymanager)
p.start_mod(__URI__)

# TOP-LEVEL CONCEPTS
I1101 = p.create_item(
    R1__has_label="physical quantity",
    R2__has_description="...",
    R4__is_instance_of=p.I2["Metaclass"],
    R18__has_usage_hint=(
        "Items such as 'voltage' or 'time' should be R4__is_instance_of-related to this item."
    )
)

I1102 = p.create_item(
    R1__has_label="physical unit",
    R2__has_description="...",
    R4__is_instance_of=p.I2["Metaclass"],
    R18__has_usage_hint= "Items such as 'Volt' or 'second' should be R4__is_instance_of-related "
    "to this item or subclasses of it."
)

I1103 = p.create_item(
    R1__has_label="SI unit",
    R2__has_description="class for units which are defined within the International System of Units",
    R3__is_subclass_of=I1102["physical unit"],
)

I1104 = p.create_item(
    R1__has_label="SI base unit",
    R2__has_description="class for units which are one of the seven base units defined within the "
    "International System of Units",
    R3__is_subclass_of=I1103["SI unit"],
    R72__is_generally_related_to="https://www.wikidata.org/wiki/Q12457",
)


I1201 = p.create_item(
    R1__has_label="second",
    R2__has_description="...",
    R4__is_instance_of=I1104["SI base unit"]
)

I1202 = p.create_item(
    R1__has_label="meter",
    R2__has_description="...",
    R4__is_instance_of=I1104["SI base unit"]
)

I1203 = p.create_item(
    R1__has_label="kilogram",
    R2__has_description="...",
    R4__is_instance_of=I1104["SI base unit"]
)

I1204 = p.create_item(
    R1__has_label="ampere",
    R2__has_description="...",
    R4__is_instance_of=I1104["SI base unit"]
)

I1205 = p.create_item(
    R1__has_label="kelvin",
    R2__has_description="...",
    R4__is_instance_of=I1104["SI base unit"]
)

I1206 = p.create_item(
    R1__has_label="mole",
    R2__has_description="...",
    R4__is_instance_of=I1104["SI base unit"]
)

I1207 = p.create_item(
    R1__has_label="candela",
    R2__has_description="...",
    R4__is_instance_of=I1104["SI base unit"]
)

# express that there are no more SI base units
p.close_class_with_R51(I1104["SI base unit"])

I1208 = p.create_item(
    R1__has_label="volt",
    R2__has_description="...",
    R4__is_instance_of=I1103["SI unit"]
)

I1209 = p.create_item(
    R1__has_label="watt",
    R2__has_description="...",
    R4__is_instance_of=I1103["SI unit"]
)

I1210 = p.create_item(
    R1__has_label="coulomb",
    R2__has_description="...",
    R4__is_instance_of=I1103["SI unit"]
)

I1211 = p.create_item(
    R1__has_label="ohm",
    R2__has_description="...",
    R4__is_instance_of=I1103["SI unit"]
)

R1200 = p.create_relation(
    R1__has_label="has associated SI unit",
    R2__has_description="Specifies the SI unit which is uniquely associated to a physical "
    "quantity.",
    R8__has_domain_of_argument_1=I1101["physical quantity"],
    R11__has_range_of_result=I1103["SI unit"],
)


I1301 = p.create_item(
    R1__has_label="electrical current",
    R2__has_description="...",
    R4__is_instance_of=I1101["physical quantity"],
    R1200__has_associated_SI_unit=I1204["ampere"],
)


I1302 = p.create_item(
    R1__has_label="electrical voltage",
    R2__has_description="...",
    R4__is_instance_of=I1101["physical quantity"],
    R1200__has_associated_SI_unit=I1208["volt"]
)

p.end_mod()
