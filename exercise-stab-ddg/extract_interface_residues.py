# ChimeraX script to rename selected residues with mutation format
import csv


alphabet = "ACDEFGHIKLMNPQRSTVWY"


def extract_interface_residues(session, parameters):
        # Ask user for structure code and adjacent chain
    params = [p for p in parameters.split(',')]
    structure_code = params[0].strip()
    adjacent_chain = params[1].strip()
    chain1_id = params[2].strip()
    chain2_id = params[3].strip()

    # Run ChimeraX command to get selected residues info
    from chimerax.core.commands import run    
    
    # Select the two chains
    run(session, f"select /{chain1_id},{chain2_id}")
    
    # Perform interface analysis
    run(session, f"contacts (/{chain1_id} & protein) restrict (/{chain2_id} & protein) sel true reveal true")

    # Get selected atoms (interface atoms)

    contact_atoms = set()

    # Loop through all models in the session
    for model in session.models.list():
        # Look for pseudobond groups named "contacts"
        print(model)
        if model.name == "contacts":
            for pb in model.pseudobonds:
                    contact_atoms.add(pb.atoms[0])
                    contact_atoms.add(pb.atoms[1])


    if not contact_atoms:
        session.logger.info("No interface atoms found.")
        return

    # Extract unique residues
    residues = set(atom.residue for atom in contact_atoms)

    # Sort residues by chain and number
    sorted_residues = sorted(residues, key=lambda r: (r.chain_id, r.number))

    # Write residues to log or file
    for res in sorted_residues:
        res_info = f"{res.one_letter_code}{res.chain_id}{res.number} {res.name} "
        session.logger.info(res_info)

    # Parse the result
    mutation_lines = []

    for i, res in enumerate(sorted_residues):
        print(res)
        for j in range(len(alphabet)):   
            try:
                # Get mutation letter from alphabet
                mutation_letter = alphabet[j]

                # Format new name
                new_name = f"{structure_code}_{chain1_id}_{adjacent_chain}, {res.one_letter_code}{res.chain_id}{res.number}{mutation_letter}"
                mutation_lines.append(new_name)

            except Exception as e:
                print(f"Error parsing line: {res}\n{e}")

    # Output the renamed lines
    for name in mutation_lines:
        print(name)

    # Define output file path (can be relative or absolute)
    output_file = "/Users/alexander.botzki/Downloads/output_data.csv"

    # Write to CSV
    with open(output_file, mode='w', newline='\n') as file:
        writer = csv.writer(file)
        writer.writerow(('#Pdb','mutation'))
        writer.writerows([c.strip() for c in r.strip(', ').split(',')]
                     for r in mutation_lines)

    # Optional: print confirmation in ChimeraX log
    session.logger.info(f"CSV file written to: {output_file}")


# To use this in ChimeraX, save it as a .py file and run it via `open <script.py>` or integrate into a ChimeraX bundle.

def register_command(logger):
    from chimerax.core.commands import register, CmdDesc, RestOfLine
    desc = CmdDesc(required = [('parameters', RestOfLine)],synopsis='Enter structure code and adjacent chain separated with a comma')
    register('extract_interface_residues', desc, extract_interface_residues, logger=logger)

register_command(session.logger)
