describe('Cypress', () => {   
    it('is working', () => {     
        expect(true).to.equal(true)   
    }) 
    
    it('opens the app', () => {   
        cy.visit('http://localhost:3000') 
    })

    it('displays add your first item button when no items have been added yet', () => {
        cy.get('button').should('exist')
    })

    it('opens form to add item', () => {
        // Check if the form exists
        cy.contains('Add your first item').click()
        cy.get('input').eq(0).should('exist')
        cy.get('input').eq(1).should('exist')
        cy.get('select').should('exist')
        cy.contains('Add Item').should('exist')

        // Fill out the form
        cy.get('input').eq(0).type('Bananas')
        cy.get('input').eq(1).type('The ripe ones')
        cy.get('select').select(1)
        cy.contains('Add Item').click()

        // Check if form does not exist
        cy.get('input').should('not.exist')
        cy.get('select').should('not.exist')
        cy.contains('Add Item').should('not.exist')

        // Check that item was added to the page
        cy.get('Bananas').should('exist')
    })
})