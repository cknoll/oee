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

I110101 = p.create_item(
    R1__has_label="Electric Current",
    R2__has_description="The flow of electric charge through a conductor."
)

I110102 = p.create_item(
    R1__has_label="Voltage",
    R2__has_description="The difference in electric potential between two points in a circuit."
)

I110103 = p.create_item(
    R1__has_label="Resistance",
    R2__has_description="The opposition to the flow of electric current in a conductor."
)

I110104 = p.create_item(
    R1__has_label="Capacitance",
    R2__has_description="The ability of a component or system to store an electric charge."
)

I110105 = p.create_item(
    R1__has_label="Inductance",
    R2__has_description="The property of a conductor that opposes changes in current."
)

I110106 = p.create_item(
    R1__has_label="Power",
    R2__has_description="The rate at which electrical energy is converted into another form of energy."
)

I110107 = p.create_item(
    R1__has_label="Energy",
    R2__has_description="The capacity to do work or transfer heat."
)

I110108 = p.create_item(
    R1__has_label="Charge",
    R2__has_description="The quantity of electricity that is transported in an electric current."
)

I110109 = p.create_item(
    R1__has_label="Conductance",
    R2__has_description="The ability of a conductor to allow current to flow through it (inverse of resistance)."
)

I110110 = p.create_item(
    R1__has_label="Impedance",
    R2__has_description="The total opposition to the flow of current in an alternating current (AC) circuit, including both resistance and reactance."
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




## Statement number 1
## Current is the flow of electric charge in a circuit.

## Statement number 2
## Resistance opposes the flow of electric current in a circuit.

## Statement number 3
## A capacitor stores electrical energy in an electric field.

## Statement number 4
## An inductor stores energy in a magnetic field when current flows through it.

## Statement number 5
## Alternating current (AC) changes direction periodically, while direct current (DC) flows in one direction.

## Statement number 6
## Electrical circuits consist of components like resistors, capacitors, inductors, and power sources.

## Statement number 7
## Capacitance is the ability to store electric charge in a system when voltage is applied.

## Statement number 8
## Inductance is the ability of a coil or circuit to oppose changes in current by generating a voltage.


## Statement number 9














p.end_mod()


