import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DocSearchPageComponent } from './doc-search-page.component';

describe('DocSearchPageComponent', () => {
  let component: DocSearchPageComponent;
  let fixture: ComponentFixture<DocSearchPageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DocSearchPageComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(DocSearchPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
