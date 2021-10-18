describe('Cypress', () => {   
    it('is working', () => {     
        expect(true).to.equal(true)   
    }) 
    
    it('opens the app', () => {   
        cy.visit('http://localhost:3000') 
    })

    it('displays add your first item button when no items have been added yet', () => {
        cy.get('.blue-button').should('exist')
    })
})