
# def cogen_section(instr: Instr, section: str)

    # write out some macro stuff if this is DISPLAY

    # write out some stuff if this is INITIALISE

    # Iterate through components,
    #  Call the same function with different arguments for each component
    #  exact call differs for INITIALISE, SAVE, FINALLY, DISPLAY

    # write out some undef macro stuff if this is DISPLAY

    # Write out a function signature
    # INITIALISE ->  int initalize(void)
    # SAVE       ->  int save(File * handle)
    # FINALLY    ->  int finally(void)
    # DISPLAY    ->  int display(void)

    # Write out different things for each of INITIALISE, SAVE, FINALLY, DISPLAY

    # If code was provided for this section in the instrument definition, print it now

    # if this is initialise, produce calls to each _{component name}_setpos()

    # Iterate through all components, getting the section code from the component
    # and adding a call to `class_{component type name}_{section}(&_{component name}_var);`
    # if the component instance defined a code block for this section

    # add some section dependent code to the end of the function definition

    # end the function, returning 0 -- always.