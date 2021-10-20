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
        cy.contains('Add your first item').click()
        cy.get('input').should('exist')
    })
})