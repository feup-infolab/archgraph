package cclasses;

public class RequestBodyClass {

    private String descriptionLevel;
    private String refCode;
    private String prodDateFrom;
    private String prodDateTo;
    private String keywords;
    private String relatedTo;
    private String creationDateFrom;
    private String creationDateTo;
    private String curatorName;
    private String interventionEndDateFrom;
    private String interventionEndDateTo;
    private String interventionStartDateFrom;
    private String interventionStartDateTo;


    public RequestBodyClass(String descriptionLevel, String refCode, String prodDateFrom, String prodDateTo, String keywords, String relatedTo, String creationDateFrom, String creationDateTo, String curatorName, String interventionEndDateFrom, String interventionEndDateTo, String interventionStartDateFrom, String interventionStartDateTo) {
        this.descriptionLevel = descriptionLevel;
        this.refCode = refCode;
        this.prodDateFrom = prodDateFrom;
        this.prodDateTo = prodDateTo;
        this.keywords = keywords;
        this.relatedTo = relatedTo;
        this.creationDateFrom = creationDateFrom;
        this.creationDateTo = creationDateTo;
        this.curatorName = curatorName;
        this.interventionEndDateFrom = interventionEndDateFrom;
        this.interventionEndDateTo = interventionEndDateTo;
        this.interventionStartDateFrom = interventionStartDateFrom;
        this.interventionStartDateTo = interventionStartDateTo;
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
        return keywords;
    }

    public void setKeywords(String keywords) {
        this.keywords = keywords;
    }

    public String getRelatedTo() {
        return relatedTo;
    }

    public void setRelatedTo(String relatedTo) {
        this.relatedTo = relatedTo;
    }

    public String getCreationDateFrom() {
        return creationDateFrom;
    }

    public void setCreationDateFrom(String creationDateFrom) {
        this.creationDateFrom = creationDateFrom;
    }

    public String getCreationDateTo() {
        return creationDateTo;
    }

    public void setCreationDateTo(String creationDateTo) {
        this.creationDateTo = creationDateTo;
    }

    public String getCuratorName() {
        return curatorName;
    }

    public void setCuratorName(String curatorName) {
        this.curatorName = curatorName;
    }

    public String getInterventionEndDateFrom() {
        return interventionEndDateFrom;
    }

    public void setInterventionEndDateFrom(String interventionEndDateFrom) {
        this.interventionEndDateFrom = interventionEndDateFrom;
    }

    public String getInterventionEndDateTo() {
        return interventionEndDateTo;
    }

    public void setInterventionEndDateTo(String interventionEndDateTo) {
        this.interventionEndDateTo = interventionEndDateTo;
    }

    public String getInterventionStartDateFrom() {
        return interventionStartDateFrom;
    }

    public void setInterventionStartDateFrom(String interventionStartDateFrom) {
        this.interventionStartDateFrom = interventionStartDateFrom;
    }

    public String getInterventionStartDateTo() {
        return interventionStartDateTo;
    }

    public void setInterventionStartDateTo(String interventionStartDateTo) {
        this.interventionStartDateTo = interventionStartDateTo;
    }
}
