package cclasses;

public class RequestBodyClass {

    private String descriptionLevel;
    private String refCode;
    private String prodDateFrom;
    private String prodDateTo;
    private String Keywords;
    private String relatedTo;


    public RequestBodyClass(String descriptionLevel, String refCode, String prodDateFrom, String prodDateTo, String keywords, String relatedTo) {
        this.descriptionLevel = descriptionLevel;
        this.refCode = refCode;
        this.prodDateFrom = prodDateFrom;
        this.prodDateTo = prodDateTo;
        Keywords = keywords;
        this.relatedTo = relatedTo;
    }

    public String getDescriptionLevel() {
        return descriptionLevel;
    }

    public void setDescriptionLevel(String descriptionLevel) {
        this.descriptionLevel = descriptionLevel;
    }

    public String getRefCode() {
        return refCode;
    }

    public void setRefCode(String refCode) {
        this.refCode = refCode;
    }

    public String getProdDateFrom() {
        return prodDateFrom;
    }

    public void setProdDateFrom(String prodDateFrom) {
        this.prodDateFrom = prodDateFrom;
    }

    public String getProdDateTo() {
        return prodDateTo;
    }

    public void setProdDateTo(String prodDateTo) {
        this.prodDateTo = prodDateTo;
    }

    public String getKeywords() {
        return Keywords;
    }

    public void setKeywords(String keywords) {
        Keywords = keywords;
    }

    public String getRelatedTo() {
        return relatedTo;
    }

    public void setRelatedTo(String relatedTo) {
        this.relatedTo = relatedTo;
    }
}
