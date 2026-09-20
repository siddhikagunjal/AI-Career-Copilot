from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from db import Base


# =====================================================
# USER MODEL
# =====================================================

class User(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    username = Column(
        String(100),
        nullable=False
    )

    email = Column(
        String(255),
        unique=True,
        nullable=False,
        index=True
    )

    password = Column(
        String(255),
        nullable=False
    )

    # Relationship with reports
    reports = relationship(
        "Report",
        back_populates="user"
    )


# =====================================================
# REPORT MODEL
# =====================================================

class Report(Base):

    __tablename__ = "reports"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    report_text = Column(
        Text,
        nullable=True
    )

    result = Column(
        Text,
        nullable=True
    )

    # Relationship with user
    user = relationship(
        "User",
        back_populates="reports"
    )