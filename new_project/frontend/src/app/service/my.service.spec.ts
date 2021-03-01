import {TestBed} from '@angular/core/testing';

import {MyService} from './my.service';

describe('ServiceService', () => {
    let service: MyService;

    beforeEach(() => {
        TestBed.configureTestingModule({});
        service = TestBed.inject(MyService);
    });

    it('should be created', () => {
        expect(service).toBeTruthy();
    });
});
