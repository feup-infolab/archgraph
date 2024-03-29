import {ComponentFixture, TestBed} from '@angular/core/testing';


import {DocumentComponent} from './document.component';

describe('MyComponent', () => {
    let component: DocumentComponent;
    let fixture: ComponentFixture<DocumentComponent>;

    beforeEach(async () => {
        await TestBed.configureTestingModule({
            declarations: [DocumentComponent]
        })
            .compileComponents();
    });

    beforeEach(() => {
        fixture = TestBed.createComponent(DocumentComponent);
        component = fixture.componentInstance;
        fixture.detectChanges();
    });

    it('should createAndUpdate', () => {
        expect(component).toBeTruthy();
    });
});
