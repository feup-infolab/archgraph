package model;

public class RequestBody {

    private String descriptionLevel;
    private String refCode;
    private String prodDateFrom;
    private String prodDateTo;
    private String keywords;
    private String relatedTo;
    private String creationDateFrom;
    private String creationDateTo;
    private String interventionEndDateFrom;
    private String interventionEndDateTo;
    private String interventionStartDateFrom;
    private String interventionStartDateTo;
    private String title;
    private String conservationCuratorName;
    private String digitalCuratorName;

    public RequestBody(String descriptionLevel, String refCode, String prodDateFrom, String prodDateTo, String keywords, String relatedTo, String creationDateFrom, String creationDateTo, String conservationCuratorName, String digitalCuratorName, String interventionEndDateFrom, String interventionEndDateTo, String interventionStartDateFrom, String interventionStartDateTo, String title) {
        this.descriptionLevel = this.getString(descriptionLevel);
        this.refCode = this.getString(refCode);
        this.prodDateFrom = this.getString(prodDateFrom);
        this.prodDateTo = this.getString(prodDateTo);
        this.keywords = this.getString(keywords);
        this.relatedTo = this.getString(relatedTo);
        this.creationDateFrom = this.getString(creationDateFrom);
        this.conservationCuratorName = this.getString(conservationCuratorName);
        this.digitalCuratorName = this.getString(digitalCuratorName);
        this.creationDateTo = this.getString(creationDateTo);
        this.interventionEndDateFrom = this.getString(interventionEndDateFrom);
        this.interventionEndDateTo = this.getString(interventionEndDateTo);
        this.interventionStartDateFrom = this.getString(interventionStartDateFrom);
        this.interventionStartDateTo = this.getString(interventionStartDateTo);
        this.title = this.getString(title);
    }

    private String getString(String identifier) {
        if (identifier != null) {
            if (!identifier.equals("")) {
                return identifier;
            } else return null;
        } else return null;
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

    public String getDigitalCuratorName() {
        return digitalCuratorName;
    }

    public void setDigitalCuratorName(String digitalCuratorName) {
        this.digitalCuratorName = digitalCuratorName;
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

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getConservationCuratorName() {
        return conservationCuratorName;
    }

    public void setConservationCuratorName(String conservationCuratorName) {
        this.conservationCuratorName = conservationCuratorName;
    }
}
