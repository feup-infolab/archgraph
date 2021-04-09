import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CreateAndUpdateDocComponent } from './create-and-update-doc.component';

describe('CreateComponent', () => {
  let component: CreateAndUpdateDocComponent;
  let fixture: ComponentFixture<CreateAndUpdateDocComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CreateAndUpdateDocComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CreateAndUpdateDocComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should createAndUpdate', () => {
    expect(component).toBeTruthy();
  });
});
